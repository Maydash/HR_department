from django.db import models

class Logos(models.Model):
    image = models.ImageField(upload_to='logo')

    class Meta:
        verbose_name = ('logo')
        verbose_name_plural = ('logolar')


class PersonEducation(models.Model):
    """Bilimi barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person')
    place_of_university = models.CharField(verbose_name='Gutaran ýeri', max_length=100)#daşary ýutdy gutaranmy ýada içerki ýokary okuw jaýy
    name_of_university = models.CharField(verbose_name='Tamamlan okuw jaýy', max_length=250)
    date_of_finishing_university = models.DateField(verbose_name='Okuwy tamamlan ýyly')
    diploma_id = models.CharField(verbose_name='Diplom belgisi', max_length=50)
    name_of_academy = models.CharField(verbose_name='Ýokary okuw jaýyndan soňky okan ýeri', max_length=200, blank=True)
    date_of_finishing_academy = models.DateField(verbose_name='Ýokary okuw jaýyndan soňky okuwy tamamlan ýyly', blank=True)
    academy_diploma_id = models.CharField(verbose_name='Akademiýanyň diplom belgisi', max_length=50, blank=True)
    remote = models.CharField(verbose_name='Gündizki', max_length=10, blank=True)
    full_time = models.CharField(verbose_name='Gaýbana', max_length=10, blank=True)
    confirmation_of_education = models.CharField(verbose_name='Daşary ýurt diplomyny ykrar edilendigi barada maglumat', max_length=250, blank=True)
    date_of_confirmation = models.DateField(verbose_name='Daşary ýurt diplomyny ykrar edilen senesi', blank=True)
    education_degree = models.CharField(verbose_name='Bilimi', max_length=50)
    major = models.CharField(verbose_name='Hünäri', max_length=100)
    scientific_degree = models.CharField(verbose_name='Hünäri', max_length=100)

    def __str__(self):
        return f'{self.name_of_university}, {self.date_of_finishing_university}'

    class Meta:
        verbose_name = 'Bilimi barada maglumat'
        verbose_name_plural = 'Bilimi barada maglumatlar'


class WasHeAbroad(models.Model):
    """Daşary ýurtda bolanmy"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_WasHeAbroad')
    name_of_country = models.CharField(verbose_name='Ýurduň ady', max_length=100)
    date = models.DateField(verbose_name='Senesi')

    def __str__(self):
        return f'{self.name_of_country}, {self.date}'

    class Meta:
        verbose_name = 'Daşary ýurtda bolandygy barada maglumat'
        verbose_name_plural = 'Daşary ýurtda bolandygy barada maglumatlar'


class StateAwards(models.Model):
    """Döwlet sylaglary barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_StateAwards')
    name_of_award = models.CharField(verbose_name='Döwlet sylagynyň ady', max_length=250)
    order_id = models.CharField(verbose_name='Permanyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Permanyň senesi')


    def __str__(self):
        return f'{self.name_of_award}, {self.order_date}'

    class Meta:
        verbose_name = 'Döwlet sylaglary barada maglumat'
        verbose_name_plural = 'Döwlet sylaglary barada maglumatlar'


class WorkExperience(models.Model):
    """Iş stažy barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_WorkExperience')
    total_experience = models.SmallIntegerField(verbose_name='Umumy iş döwri')
    experience_in_court = models.SmallIntegerField(verbose_name='Kazyýetde iş döwri')
    experience_in_army = models.SmallIntegerField(verbose_name='Harby gulluk döwri')
    experience_in_education = models.SmallIntegerField(verbose_name='Ýokary okuw döwri')
    experience_in_last_position = models.SmallIntegerField(verbose_name='Soňky wezipedäki iş döwri')

    def __str__(self):
        return f'{self.total_experience}, {self.experience_in_court}'

    class Meta:
        verbose_name = 'Iş stažy barada maglumat'
        verbose_name_plural = 'Iş stažy barada maglumatlar'


class ParticipateInElections(models.Model):
    """Saýlawly edaralara gatnaşmagy"""
    note = models.CharField(verbose_name='Bellik', max_length=250)


class Punishment(models.Model):
    """Düzgün nyzam jogapkärçiligine çekilmegi barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_Punishment')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Düzgün nyzam jogapkärçiligine çekilmegi barada maglumat'
        verbose_name_plural = 'Düzgün nyzam jogapkärçiligine çekilmegi barada maglumatlar'


class AppreciationLetter(models.Model):
    """Hormat hatlary barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_AppreciationLetter')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Hormat hatlary barada maglumat'
        verbose_name_plural = 'Hormat hatlary barada maglumatlar'


class Rewards(models.Model):
    """Döşe dakylýan nyşany barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_Rewards')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Döşe dakylýan nyşany barada maglumat'
        verbose_name_plural = 'Döşe dakylýan nyşany barada maglumatlar'


class Vacation(models.Model):
    """Esasy zähmet rugsady barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_Vacation')
    name= models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Esasy zähmet rugsady barada maglumat'
        verbose_name_plural = 'Esasy zähmet rugsady barada maglumatlar'


class AdditionalVacation(models.Model):
    """Goşmaça rugsady barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_AdditionalVacation')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Goşmaça rugsady barada maglumat'
        verbose_name_plural = 'Goşmaça rugsady barada maglumatlar'


class HealthVacation(models.Model):
    """Zähmete ukypsyzlgy boýunça rugsady barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_HealthVacation')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Zähmete ukypsyzlgy boýunça rugsady barada maglumat'
        verbose_name_plural = 'Zähmete ukypsyzlgy boýunça rugsady barada maglumatlar'


class UnpaidLeave(models.Model):
    """Tölegsiz zähmet rugsady barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_UnpaidLeave')
    name = models.CharField(verbose_name='Ady', max_length=250)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')

    def __str__(self):
        return f'{self.name}, {self.order_date}'

    class Meta:
        verbose_name = 'Tölegsiz rugsady barada maglumat'
        verbose_name_plural = 'Tölegsiz rugsady barada maglumatlar'


class BusinessTrip(models.Model):
    """Iş sapary barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_BusinessTrip')
    name_of_country = models.CharField(verbose_name='Ýurduň ady', max_length=100)
    order_id = models.CharField(verbose_name='Buýrugyň belgisi', max_length=20)
    order_date = models.DateField(verbose_name='Buýrugyň senesi')
    start_date = models.DateField(verbose_name='Giden senesi')
    end_date = models.DateField(verbose_name='Gelen senesi')

    def __str__(self):
        return f'{self.name_of_country}, {self.start_date}'

    class Meta:
        verbose_name = 'Iş sapary barada maglumat'
        verbose_name_plural = 'Iş sapary barada maglumatlar'


class CarInfo(models.Model):
    """Awtoulagy barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_CarInfo')
    name = models.CharField(verbose_name='Awtoulagyň ady', max_length=70)
    date_manufacture = models.DateField(verbose_name='Öndürilen senesi')
    is_own = models.CharField(verbose_name='Awtoulag kimiň adyna resmilleşdirilen', max_length=100)

    def __str__(self):
        return f'{self.name}, {self.date_manufacture}'

    class Meta:
        verbose_name = 'Awtoulagy barada maglumat'
        verbose_name_plural = 'Awtoulagy barada maglumatlar'


class CriminalLiability(models.Model):
    """Ýakyn garyndalaşlary jenaýat jogapkärçiligi barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_CriminalLiability')
    name = models.CharField(verbose_name='Ady', max_length=200)
    date = models.DateField(verbose_name='Senesi')
    court_info = models.CharField(verbose_name='Ady', max_length=200)

    def __str__(self):
        return f'{self.name}, {self.date}'

    class Meta:
        verbose_name = 'Ýakyn garyndalaşlary jenaýat jogapkärçiligi barada maglumat'
        verbose_name_plural = 'Ýakyn garyndalaşlary jenaýat jogapkärçiligi barada maglumatlar'


class RelativesLivingAbroad(models.Model):
    """Ýakyn garyndalaşlary daşary ýurtda ýaşaýanlar barada maglumat"""
    # person = models.ForeignKey(PersonInformation, on_delete=models.CASCADE, verbose_name='Işgär', related_name='person_RelativesLivingAbroad')
    name = models.CharField(verbose_name='Ady, Familiýasy', max_length=200)
    country_name = models.CharField(verbose_name='Ýurduň ady', max_length=100)
    start_date = models.DateField(verbose_name='Giden senesi')
    end_date = models.DateField(verbose_name='Gelen senesi')

    def __str__(self):
        return f'{self.name}, {self.country_name}'

    class Meta:
        verbose_name = 'Ýakyn garyndalaşlary daşary ýurtda ýaşaýanlar barada maglumat'
        verbose_name_plural = 'Ýakyn garyndalaşlary daşary ýurtda ýaşaýanlar barada maglumatlar'


class PersonInformation(models.Model):
    """Esasy model"""
    image = models.ImageField(upload_to='person_photo')#TODO: surat ýüklenýän ýerini maslahatlaşmaly
    last_name = models.CharField(verbose_name='Familiýasy', max_length=100)
    first_name = models.CharField(verbose_name='Ady', max_length=100)
    patronic_name = models.CharField(verbose_name='Atasynyň ady', max_length=100)
    second_name = models.CharField(verbose_name='Gyz familiýasy', max_length=100)
    begining_of_work = models.DateField(verbose_name='Işe giren senesi:')
    degree_of_work = models.CharField(verbose_name='Buýrugyň belgisi', max_length=50, blank=True)
    order_of_work = models.CharField(verbose_name='Perkanyň belgisi', max_length=50, blank=True)
    birth_certificate_id = models.CharField(verbose_name='Dogluş hakynda şahadatnamasynyň belgisi', max_length=50)
    passport_id = models.CharField(verbose_name='Pasport belgisi', max_length=50)
    passport_address = models.CharField(verbose_name='Pasport belgisi', max_length=250)
    passport_date = models.DateField(verbose_name='Pasport berlen senesi')
    date_of_birthday = models.DateField(verbose_name='Doglan senesi')
    #TODO: yaşyny hasaplamaly
    birthday_place = models.CharField(verbose_name='Doglan ýeri', max_length=250)
    citizenship = models.CharField(verbose_name='Raýatlylygy', max_length=100)
    nationality = models.CharField(verbose_name='Milleti', max_length=100)
    address = models.CharField(verbose_name='Ýazgyda duran salgysy', max_length=250)
    exactly_address = models.CharField(verbose_name='Hakyky salgysy salgysy', max_length=250)
    person_education = models.ForeignKey(PersonEducation, on_delete=models.CASCADE, verbose_name='Bilimi barada maglumat', related_name='person_education')
    was_he_abroad = models.ForeignKey(WasHeAbroad, on_delete=models.CASCADE, verbose_name='Daşary ýurtda bolanmy', related_name='was_he_abroad')
    state_awards = models.ForeignKey(StateAwards, on_delete=models.CASCADE, verbose_name='Döwlet sylaglary barada maglumat', related_name='state_awards')
    work_experience = models.ForeignKey(WorkExperience, on_delete=models.CASCADE, verbose_name='Iş stažy barada maglumat', related_name='work_experience')
    participate_in_elections = models.ForeignKey(ParticipateInElections, on_delete=models.CASCADE, verbose_name='Saýlawly edaralara gatnaşmagy', related_name='participate_in_elections')
    punishment = models.ForeignKey(Punishment, on_delete=models.CASCADE, verbose_name='Düzgün nyzam jogapkärçiligine çekilmegi barada maglumat', related_name='punishment')
    appreciation_letter = models.ForeignKey(AppreciationLetter, on_delete=models.CASCADE, verbose_name='Hormat hatlary barada maglumat', related_name='appreciation_letter')
    rewards = models.ForeignKey(Rewards, on_delete=models.CASCADE, verbose_name='Döşe dakylýan nyşany barada maglumat',related_name='rewards')
    vacation = models.ForeignKey(Vacation, on_delete=models.CASCADE, verbose_name='Esasy zähmet rugsady barada maglumat',related_name='vacation')
    additional_vacation = models.ForeignKey(AdditionalVacation, on_delete=models.CASCADE, verbose_name='Goşmaça rugsady barada maglumat',related_name='additional_vacation')
    health_vacation = models.ForeignKey(HealthVacation, on_delete=models.CASCADE, verbose_name='Zähmete ukypsyzlgy boýunça rugsady barada maglumat',related_name='health_vacation')
    unpaid_leave = models.ForeignKey(UnpaidLeave, on_delete=models.CASCADE, verbose_name='Tölegsiz zähmet rugsady barada maglumat',related_name='unpaid_leave')
    business_trip = models.ForeignKey(BusinessTrip, on_delete=models.CASCADE, verbose_name='Iş sapary barada maglumat',related_name='business_trip')
    car_info = models.ForeignKey(CarInfo, on_delete=models.CASCADE, verbose_name='Awtoulagy barada maglumat',related_name='car_info')
    criminal_liability = models.ForeignKey(CriminalLiability, on_delete=models.CASCADE, verbose_name='Ýakyn garyndalaşlary jenaýat jogapkärçiligi barada maglumat',related_name='criminal_liability')
    relatives_living_abroad = models.ForeignKey(RelativesLivingAbroad, on_delete=models.CASCADE, verbose_name='Ýakyn garyndalaşlary daşary ýurtda ýaşaýanlar barada maglumat',related_name='relatives_living_abroad')
    foreign_languages = models.CharField(verbose_name='Haýsy daşary ýurt dillerini bilýär', max_length=100)
    is_election = models.CharField(verbose_name='Saýlawly edaralara gatnaşmagy', max_length=100)
    height = models.SmallIntegerField(verbose_name='Boýy')
    weight = models.SmallIntegerField(verbose_name='Agramy')
    phone_number = models.CharField(verbose_name='Telefon belgisi', max_length=12, blank=True)
    phone_number_1 = models.CharField(verbose_name='Telefon belgisi 2', max_length=12, blank=True)
    marital_status = models.CharField(verbose_name='Maşgala ýagdaýy', max_length=100)
    file = models.FileField(upload_to='files/', blank=True)
    # TODO: maglumatlary word doc ýüklemek

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        verbose_name = 'Işgär'
        verbose_name_plural = 'Işgärler'