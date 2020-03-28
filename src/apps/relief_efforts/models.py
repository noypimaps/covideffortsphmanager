import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField


class ReliefEfforts(models.Model):
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
    RELIEF_TYPES = (
        ('frontliner', 'frontliner'),
        ('families', 'families'),
        ('public', 'public'),
        ('supplier', 'supplier'),
        ('testing kit for PUI', 'testing kit for PUI'),
        ('other service personel', 'other service personel'),
        ('other', 'other')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    relief_name = models.CharField(max_length=999, null=False)
    contact_details = models.TextField(blank=True, default='N/A')
    severity_urgency = models.CharField(max_length=50, blank=False, default='N/A')
    status = models.CharField(max_length=50, blank=False, default='N/A')
    needs = models.TextField(blank=False, default='N/A')
    org_type = models.CharField(max_length=50, blank=False, choices=ORG_TYPES, default='other')
    relief_type = models.CharField(max_length=999, blank=False, choices=RELIEF_TYPES, default='other')
    update_date = models.DateTimeField(auto_now_add=True)
    link_for_more_info = models.TextField(default='N/A', blank=False)
    other_info = JSONField(null=True, blank=True)

    class Meta:
        ordering=('-update_date',)
        verbose_name_plural = "Relief Efforts"

    def __str__(self):
        return str(self.id)

