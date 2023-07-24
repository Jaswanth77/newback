from rest_framework import serializers
from .models import ApplicationFormModel
import os
class ApplicationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationFormModel
        exclude = ("ar_number",)

    student_photo = serializers.ImageField(required=False)
    neet_score_card = serializers.FileField(required=False)
    conduct_certificate = serializers.FileField(required=False)
    neet_admit_card = serializers.FileField(required=False)
    allotment_order_sslc_certificate = serializers.FileField(required=False)
    hsc_certificate = serializers.FileField(required=False)
    transfer_certificate = serializers.FileField(required=False)
    community_certificate = serializers.FileField(required=False)
    aadhaar_card = serializers.FileField(required=False)
    eligibility_migration_certificates = serializers.FileField(required=False)
    nativity_certificate = serializers.FileField(required=False)
    income_certificate = serializers.FileField(required=False)
    physical_fitness_certificate = serializers.FileField(required=False)
    declaration_form = serializers.FileField(required=False)
    anti_ragging_bond = serializers.FileField(required=False)
    physically_handicapped_certificate = serializers.FileField(required=False)

    def create(self, validated_data):
        instance = super().create(validated_data)

        field_mapping = {
            'student_photo': 'student_photo.jpg',
            'neet_score_card': 'neet_score_card.pdf',
            'conduct_certificate': 'conduct_certificate.pdf',
            'neet_admit_card': 'neet_admit_card.pdf',
            'allotment_order_sslc_certificate': 'allotment_order_sslc_certificate.pdf',
            'hsc_certificate': 'hsc_certificate.pdf',
            'transfer_certificate': 'transfer_certificate.pdf',
            'community_certificate': 'community_certificate.pdf',
            'aadhaar_card': 'aadhaar_card.pdf',
            'eligibility_migration_certificates': 'eligibility_migration_certificates.pdf',
            'nativity_certificate': 'nativity_certificate.pdf',
            'income_certificate': 'income_certificate.pdf',
            'physical_fitness_certificate': 'physical_fitness_certificate.pdf',
            'declaration_form': 'declaration_form.pdf',
            'anti_ragging_bond': 'anti_ragging_bond.pdf',
            'physically_handicapped_certificate': 'physically_handicapped_certificate.pdf',
        }

        for field_name, filename in field_mapping.items():
            file_data = validated_data.pop(field_name, None)
            if file_data:
                file_field = getattr(instance, field_name)
                new_file_name = f"{instance.ar_number}_{filename}"
                file_path = file_field.path
                new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
                os.rename(file_path, new_file_path)
                file_field.name = new_file_path.split("/")[-1]
                setattr(instance, field_name, file_field)

        instance.save()
        return instance
    
    # def update(self,instance,validated_data):
    #     print("hello")
    #     print("neet_score_card:"+instance.neet_score_card)
    #     neet_score_card = validated_data.get('neet_score_card',None)
    #     conduct_certificate =validated_data.get('conduct_certificate',None)
    #     neet_admit_card = validated_data.get('neet_admit_card',None)
    #     allotment_order_sslc_certificate = validated_data.get('allotment_order_sslc_certificate',None)
    #     hsc_certificate = validated_data.get('hsc_certificate',None)
    #     transfer_certificate = validated_data.get('transfer_certificate',None)
    #     community_certificate = validated_data.get('community_certificate',None)
    #     aadhaar_card = validated_data.get('aadhaar_card',None)
    #     eligibility_migration_certificates = validated_data.get('eligibility_migration_certificates',None)
    #     nativity_certificate = validated_data.get('nativity_certificate',None)
    #     income_certificate = validated_data.get('income_certificate',None)
    #     physical_fitness_certificate = validated_data.get('physical_fitness_certificate',None)
    #     declaration_form = validated_data.get('declaration_form',None)
    #     anti_ragging_bond = validated_data.get('anti_ragging_bond',None)
    #     physically_handicapped_certificate = validated_data.get('physically_handicapped_certificate',None)

    #     if neet_score_card:
    #         instance.neet_score_card.delete()  
    #         instance.neet_score_card.save(neet_score_card.name, neet_score_card)

    #     if conduct_certificate:
    #         instance.conduct_certificate.delete()  # Delete the existing file
    #         instance.conduct_certificate.save(conduct_certificate.name, conduct_certificate)  # Save the new file

    #     if neet_admit_card:
    #         instance.neet_admit_card.delete()  # Delete the existing file
    #         instance.neet_admit_card.save(neet_admit_card.name, neet_admit_card)  # Save the new file

    #     if allotment_order_sslc_certificate:
    #         instance.allotment_order_sslc_certificate.delete()  # Delete the existing file
    #         instance.allotment_order_sslc_certificate.save(allotment_order_sslc_certificate.name, allotment_order_sslc_certificate)  # Save the new file

    #     if hsc_certificate:
    #         instance.hsc_certificate.delete()  # Delete the existing file
    #         instance.hsc_certificate.save(hsc_certificate.name, hsc_certificate)  # Save the new file

    #     if transfer_certificate:
    #         instance.transfer_certificate.delete()  # Delete the existing file
    #         instance.transfer_certificate.save(transfer_certificate.name,transfer_certificate )  # Save the new file

    #     if community_certificate:
    #         instance.community_certificate.delete()  # Delete the existing file
    #         instance.community_certificate.save(community_certificate.name, community_certificate)  # Save the new file

        
    #     if aadhaar_card:
    #         instance.aadhaar_card.delete()  # Delete the existing file
    #         instance.aadhaar_card.save(aadhaar_card.name, aadhaar_card)  # Save the new file

    #     if eligibility_migration_certificates:
    #         instance.eligibility_migration_certificates.delete()  # Delete the existing file
    #         instance.eligibility_migration_certificates.save(eligibility_migration_certificates.name, eligibility_migration_certificates)  # Save the new file

    #     if nativity_certificate:
    #         instance.nativity_certificate.delete()  # Delete the existing file
    #         instance.nativity_certificate.save(nativity_certificate.name, nativity_certificate)  # Save the new file

    #     if income_certificate:
    #         instance.income_certificate.delete()  # Delete the existing file
    #         instance.income_certificate.save(income_certificate.name,income_certificate )  # Save the new file

    #     if physical_fitness_certificate:
    #         instance.physical_fitness_certificate.delete()  # Delete the existing file
    #         instance.physical_fitness_certificate.save(physical_fitness_certificate.name, physical_fitness_certificate)  # Save the new file


    #     if declaration_form:
    #         instance.declaration_form.delete()  # Delete the existing file
    #         instance.declaration_form.save(declaration_form.name, declaration_form)  # Save the new file

    #     if anti_ragging_bond:
    #         instance.anti_ragging_bond.delete()  # Delete the existing file
    #         instance.anti_ragging_bond.save(anti_ragging_bond.name, anti_ragging_bond)  # Save the new file
        
    #     if physically_handicapped_certificate:
    #         instance.physically_handicapped_certificate.delete()  # Delete the existing file
    #         instance.physically_handicapped_certificate.save(physically_handicapped_certificate.name, physically_handicapped_certificate)  # Save the new file

    #     instance.save
    #     return instance


