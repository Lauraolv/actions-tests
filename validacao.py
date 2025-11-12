import re

def validar_email(email):
    """
    Verifica se um e-mail possui um formato minimamente válido.
    
    Regras:
    1. Deve ser uma string.
    2. Deve conter exatamente um '@'.
    3. Deve conter pelo menos um '.' após o '@'.
    4. O '@' não pode ser o primeiro caractere.
    5. O '.' não pode ser o último caractere após o '@'.
    """
    
    if not isinstance(email, str):
        return False
        
    if email.count('@') != 1:
        return False
        
    if email.startswith('@'):
        return False
        
    local_part, domain_part = email.split('@')
    
    if '.' not in domain_part:
        return False
        
    if domain_part.endswith('.'):
        return False
        
    return True