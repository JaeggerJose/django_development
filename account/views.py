from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
#system import
import os, json
from subprocess import getoutput
from app.models import User

def get_uid():
    get_uid = '/tmp/ldap_templates/uidlist.conf'
    id_get  = open(get_uid, 'r')
    gid_uid = id_get.read(5)
    id_get.close()
    int_gid_uid= int(gid_uid)
    return int_gid_uid

def ldap_write_user_and_group_file(request):
    name = "maghsuan"
    fopen_file = '/tmp/ldap_templates/{}_user_group_creattion.ldif'.format(name)
#    get_uid = '/tmp/ldap_templates/uidlist.conf'
#    id_get  = open(get_uid, 'r')
#    gid_uid = id_get.read(5)
#    id_get.close()
    gid_uid = get_uid()
    #= data['name']
    
    f = open(fopen_file,'w+')
    f.write("dn: cn={},ou=Group,dc=ccllab,dc=edu,dc=tw\n".format(name))
    f.write("cn: {}\n".format(name))
    f.write("gidNumber: {}\n".format(gid_uid))
    f.write("objectClass: top\n")
    f.write("objectClass: posixGroup\n")
    f.write("memberUid: {}\n\n".format(name))
    f.write("dn: uid={},ou=User,dc=ccllab,dc=edu,dc=tw\n".format(name))
    f.write("cn: {}\n".format(name))
    f.write("givenName: {}\n".format(name))
    f.write("sn: {}\n".format(name))
    f.write("uid: {}\n".format(name))
    f.write("uidNumber: {}\n".format(gid_uid))
    f.write("gidNumber: {}\n".format(gid_uid))
    f.write("homeDirectory: /home/{}\n".format(name))
    f.write("loginShell: /bin/bash\n")
    f.write("objectClass: top\nobjectClass: posixGroup\nobjectClass: inetOrgPerson\nobjectClass: shadowAccount\n")
    f.write("shadowFlag: 0\nshadowMin: 0\nshadowMax: 99999\nshadowWarning: 0\nshadowInactive: 99999\nshadowLastChange: 12011\n shadowExpire: 99999\n")
    f.write("userPassword: {}".format(name))
    f.close()
    id_plus  = open(get_uid, 'w+')
    print(gid_uid)
    int_gid_uid+=1
    id_plus.write("{}".format(int_gid_uid))
    id_plus.close()
    uidgm = {'u_g_id' : gid_uid }
    return JsonResponse(uidgm)
    
def ldap_create_user_and_group(data):
    ldap_write_user_and_group_file(data)
    name = data['name']
    file_location = '/tmp/ldap_templates/{}_user_group_creattion.ldif'.format(name)
    ldap_add_command = 'ldapadd -cx -h 120.126.17.200:3899 -D "cn=admin,dc=ccllab,dc=edu,dc=tw" -w -f file_location'
    return 0

def save_user_information_into_database(data):
    user_name = data['name']
    uid = get_uid()
    added_user = User.objects.create(id=uid, name=user_name, telephone="+886968920183", email="index@praexisio.com")
    added_user.save()
    print("user added into database")
    return 0

#def create_new_account(request):
#    data = json.loads(request.body.decode('utf-8'))
#    
#    ldap_write_user_and_group_file(data)#    ldap_create_user_and_group(data)
#    print "ldap-user and  ldap-group have been created in server"
#    print "Next will add user information into database"
#    save_user_information_into_database(data)
#    create_user_for_slurm_system(data)
#    return 0
