import uuid

from django.db import models


class Organizations(models.Model):
    ORG_TYPES = (
        ('hospital', 'hospital'),
        ('organization', 'organization'),
        ('business', 'business'),
        ('supplier', 'supplier'),
        ('research', 'research'),
        ('facility', 'facility'),
        ('lgu', 'lgu'),
        ('personal', 'personal'),
        ('other', 'other')
    )
    SEVERITY_TYPES = (
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    org_name = models.CharField(max_length=999, null=False)
    severity_urgency = models.CharField(max_length=50, choices=SEVERITY_TYPES, default='low')
    status = models.CharField(max_length=50, blank=False, default='unverified')
    org_type = models.CharField(max_length=50, blank=False, choices=ORG_TYPES, default='other')
    update_date = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Organizations"

    def __str__(self):
        return str(self.org_name)

class ContactDetails(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    contact_number = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Contact Details"

    def __str__(self):
        return str(self.name)


class BankDetails(models.Model):
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100, null=False)
    account_name = models.CharField(max_length=100, null=False)
    account_number = models.CharField(max_length=100, null=False)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Bank Details"

    def __str__(self):
        return str(self.bank_name)


class PricingDetails(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    name_of_item = models.CharField(max_length=100, null=False)
    unit = models.CharField(max_length=100, null=False)
    unit_price = models.CharField(max_length=100, null=False)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Pricing Details"

    def __str__(self):
        return str(self.bank_name)


class AddressDetails(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    unit_no = models.CharField(max_length=10, null=True, blank=True)
    building_name = models.CharField(max_length=100, null=True, blank=True)
    street = models.TextField()
    brgy = models.TextField()
    city_municipality = models.TextField()
    province = models.TextField()
    region = models.TextField()
    postal_code = models.TextField(null=True, blank=True)

    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Address Details"

    def __str__(self):
        return str(self.id)


class OtherDetails(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    what_they_do = models.TextField(default="N/A")
    who_they_help = models.TextField(default="N/A")
    link_for_more_info = models.TextField(null=False, default="N/A")
    link_to_poster = models.TextField(null=False, default="N/A")
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Other Details"

    def __str__(self):
        return str(self.id)


class ItemizedNeeds(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    name_of_item = models.CharField(max_length=100, null=False)
    unit = models.CharField(max_length=100, null=False)
    received_inventories = models.IntegerField(default=0)
    total_need = models.IntegerField(default=0)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Itemized Needs"

    def __str__(self):
        return str(self.id)