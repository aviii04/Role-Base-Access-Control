from apps.authentication.authenticate.models import FeatureRolePrivilege, UserDetails, PartnerFeature, UserRole

# This Module defines generic functions common to all Apps.

def getUserPrivileges(userId):
    userRoles = getUserRoles(userId)
    userFeatures = getUserFeatures(userId)
    return [userPrivilege.privilege for userPrivilege in
            FeatureRolePrivilege.objects.filter(feature__in=userFeatures).filter(role__in=userRoles)]

def getUserFeatures(userId):
    userDetail = UserDetails.objects.get(user=userId)
    if userDetail.partner:
        return getFeatures(userDetail.partner.id)
    else:
        return getFeatures(userId)

def getFeatures(userId):
    return [partnerFeature.feature for partnerFeature in PartnerFeature.objects.filter(partner__exact=userId)]

def getUserRoles(userId):
    return [userRole.role for userRole in UserRole.objects.filter(user__exact=userId)]
