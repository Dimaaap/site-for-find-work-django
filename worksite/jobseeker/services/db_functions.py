def select_all_fields_from_model(model: callable):
    queryset = model.objects.all()
    return queryset

