from django.db import models
# accountsアプリのmodelモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Specialist(models.Model):
    # 診療科のフィールド
    specialist = models.CharField(
        verbose_name='診療科',
        max_length=20
    )

    def __str__(self):
        return self.specialist

class Record(models.Model):
    '''記録されたデータを管理するモデル'''
    # CustomUserモデル(のuser_id)とRecordモデルを
    # 1対多の関係で結び付ける
    # CustomerUserが親でRecordが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        verbose_name='担当医',
        on_delete=models.PROTECT
    )

    # SpecialistモデルとRecordモデルを
    # 1対多の関係で結び付ける
    # Specialistが親でRecordが子の関係となる
    specialist = models.ForeignKey(
        Specialist,
        verbose_name='診療科',
        on_delete=models.PROTECT
    )

    # 患者氏名
    patient_name = models.CharField(
        verbose_name='患者氏名',
        max_length=20
    )
    # 生年月日
    birthday = models.CharField(
        verbose_name='生年月日',
        max_length=8
    )
    # 性別
    gender = models.CharField(
        verbose_name='性別',
        max_length=4
    )
    # 電話番号
    tel_number = models.CharField(
        verbose_name='電話番号',
        max_length=11
    )
    # 住所
    address = models.CharField(
        verbose_name='住所',
        max_length=100
    )
    # 病状
    condition = models.TextField(
        verbose_name='病状',
    )
    # イメージのフィールド1
    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to='attachment',
        blank=True,
        null=True
    )
    # イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='attachment',
        blank=True,
        null=True
    )
    # イメージのフィールド3
    image3 = models.ImageField(
        verbose_name='イメージ３',
        upload_to='attachment',
        blank=True,
        null=True
    )
    # 記録日時のフィールド
    record_at = models.DateTimeField(
        verbose_name='記録日時',
        auto_now_add=True
    )

    def __str__(self):
        return f"Record for {self.patient_name} - Specialist: {self.specialist.specialist}"

