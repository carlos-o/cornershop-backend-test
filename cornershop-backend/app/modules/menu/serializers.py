from rest_framework import serializers


class OptionSerializers(serializers.Serializer):
	id = serializers.IntegerField()
	description = serializers.CharField()
	created_at = serializers.DateTimeField()


class MenuSerializers(serializers.Serializer):
	id = serializers.IntegerField()
	name = serializers.CharField()
	description = serializers.CharField()
	start_date = serializers.DateField()
	created_at = serializers.DateTimeField()
	options = serializers.SerializerMethodField()

	def get_options(self, obj):
		options = OptionSerializers(obj.option_menu.all(), many=True).data
		return options

