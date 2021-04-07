class TaskSerializer(serializers.ModelSerializer):
    project = serializers.HiddenField(default=CurrentProjectDefault())

    def create(self, validated_data):
        instance = Task(**validated_data)
        instance.save()
        return instance
   
    class Meta:
        model = Task
        fields = ("id", "name", "project", "description", "last_modified")
        read_only_fields = ("id", "last_modified")
