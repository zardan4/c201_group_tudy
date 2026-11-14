from datetime import timedelta

import stations, bike, client_balance, sessions, datetime

bike1 = bike.ElectricBike(1, 78)
bike2 = bike.ElectricBike(2, 98)
bike3 = bike.RegularBike(3)
bike4 = bike.RegularBike(4)
bike5 = bike.ElectricBike(5, 45)

Station1 = stations.Station([bike1, bike2])
Station2 = stations.Station([bike3, bike4, bike5])
Bikenet = stations.Network([Station1, Station2])

Olga = client_balance.Client("Olga", 100)
Daniil = client_balance.Client("Olga", 150)

assert Station1.take_bike(2, Olga), "bike couldn't be taken"
Olga.session.time_start = datetime.datetime.now() - timedelta(minutes=2)
Station1.return_bike(Olga)

assert not Station1.take_bike(3, Daniil), "bike is not supposed to be taken"

assert Station2.take_bike(5, Daniil), "bike couldn't be taken"
Daniil.session.time_start = datetime.datetime.now() - timedelta(minutes=10)
Station2.return_bike(Daniil)

assert Station1.take_bike(2, Olga), "bike couldn't be taken"
Olga.session.time_start = datetime.datetime.now() - timedelta(minutes=5)
Station1.return_bike(Olga)



Station1.return_bike(Olga)
Station2.return_bike(Daniil)
print(f"Баланс {Olga.name}:{Olga.get_balance()}")
print(f"Баланс {Daniil.name}:{Daniil.get_balance()}")

print(Bikenet.get_balance())


