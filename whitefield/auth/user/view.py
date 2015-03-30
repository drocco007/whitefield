def as_json(user):
    return {
        'full_name': user.full_name,
        'school': user.school,
    }
