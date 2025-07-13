
from django.db import models

class BMBCChecksheet(models.Model):
    adjustingTube = models.CharField(max_length=100)
    cylinderBody = models.CharField(max_length=100)
    pistonTrunnion = models.CharField(max_length=100)
    plungerSpring = models.CharField(max_length=100)

class BogieChecksheet(models.Model):
    axleGuide = models.CharField(max_length=100)
    bogieFrameCondition = models.CharField(max_length=100)
    bolster = models.CharField(max_length=100)
    bolsterSuspensionBracket = models.CharField(max_length=100)
    lowerSpringSeat = models.CharField(max_length=100)

class BogieDetails(models.Model):
    bogieNo = models.CharField(max_length=100)
    dateOfIOH = models.DateField()
    deficitComponents = models.CharField(max_length=255)
    incomingDivAndDate = models.CharField(max_length=100)
    makerYearBuilt = models.CharField(max_length=100)

class BogieForm(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bmbcChecksheet = models.OneToOneField(BMBCChecksheet, on_delete=models.CASCADE)
    bogieChecksheet = models.OneToOneField(BogieChecksheet, on_delete=models.CASCADE)
    bogieDetails = models.OneToOneField(BogieDetails, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="Saved")

class WheelSpecificationFields(models.Model):
    axleBoxHousingBoreDia = models.CharField(max_length=100, blank=True)
    bearingSeatDiameter = models.CharField(max_length=100, blank=True)
    condemningDia = models.CharField(max_length=100, blank=True)
    intermediateWWP = models.CharField(max_length=100, blank=True)
    lastShopIssueSize = models.CharField(max_length=100, blank=True)
    rollerBearingBoreDia = models.CharField(max_length=100, blank=True)
    rollerBearingOuterDia = models.CharField(max_length=100, blank=True)
    rollerBearingWidth = models.CharField(max_length=100, blank=True)
    treadDiameterNew = models.CharField(max_length=100, blank=True)
    variationSameAxle = models.CharField(max_length=100, blank=True)
    variationSameBogie = models.CharField(max_length=100, blank=True)
    variationSameCoach = models.CharField(max_length=100, blank=True)
    wheelDiscWidth = models.CharField(max_length=100, blank=True)
    wheelGauge = models.CharField(max_length=100, blank=True)
    wheelProfile = models.CharField(max_length=100, blank=True)

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50, unique=True)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.OneToOneField(WheelSpecificationFields, on_delete=models.CASCADE)



# Create your models here.
