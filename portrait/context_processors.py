from .models import Portrait


def portrait_pic(request): 
    if request.user.is_authenticated:
        portrait_obj = Portrait.objects.get(user=request.user)
        pic = portrait_obj.image        
        return {'picture':pic}
    return {}
