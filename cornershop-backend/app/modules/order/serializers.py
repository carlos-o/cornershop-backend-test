from rest_framework import serializers


class OrderSerializers(serializers.Serializer):
	id = serializers.IntegerField()
	menu = serializers.SerializerMethodField()
	rut = serializers.SerializerMethodField()
	name = serializers.SerializerMethodField()
	option = serializers.SerializerMethodField()
	customization = serializers.CharField()
	created_at = serializers.DateTimeField()

	def get_menu(self, obj):
		return obj.option.menu.name

	def get_rut(self, obj):
		return obj.user.rut

	def get_name(self, obj):
		full_name = obj.user.first_name + " " + obj.user.last_name
		return full_name

	def get_option(self, obj):
		return obj.option.description
