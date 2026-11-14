class Client:

    def __init__(self, name:str, balance:float):
#Параметри:
#name (str) - це імʼя самого клієнта
#balance (float) - баланс клієнта у гривнях
   def minus_money(self, amount:float):
       if self.balance >=  amount:
           self.balance -= amount
           return True # cписує суму з балансу, True якщо грошей вистачило, False
       else:
           return False

    def get_balance(self):
        return self.balance # перевіряє поточний баланс юзера




