from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'donaciones': True,
        'rifas': True,
        'usuarios':True,
        'escolar': True,
        'expedientes': True,
        'adopciones': True,
        'medico': True,
        'expedientes': True,
    }

class Consejo(AbstractUserRole):
    available_permissions = {
        'donaciones': True,
        'rifas': True,
        'usuarios': True,
        'escolar': True,
    }
    
    
class Expedientes(AbstractUserRole):
    available_permissions = {
        'expedientes': True,
    }
    
    
class Medico(AbstractUserRole):
    available_permissions = {
        'medico': True,
    }
    
    
class Adopciones(AbstractUserRole):
    available_permissions = {
        'adopciones': True,
        'donaciones': True,
    }