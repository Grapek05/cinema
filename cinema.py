class Movie:
    def __init__(self, title, duration, showtimes):
        self.title = title
        self.duration = duration
        self.showtimes = showtimes

    def add_showtime(self, time):
        """Dodaje nową godzinę seansu."""
        if time not in self.showtimes:
            self.showtimes.append(time)
        else:
            print(f"Seans o godzinie {time} już istnieje.")

    def remove_showtime(self, time):
        """Usuwa godzinę seansu."""
        if time in self.showtimes:
            self.showtimes.remove(time)
        else:
            print(f"Seans o godzinie {time} nie istnieje.")

    def display_details(self):
        """Wyświetla szczegóły filmu."""
        print(f"Film: {self.title}")
        print(f"Czas trwania: {self.duration} minut")
        print(f"Godziny seansów: {', '.join(self.showtimes)}")


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations = []

    def add_reservation(self, movie, time):
        """Dodaje rezerwację na dany film i godzinę."""
        if time in movie.showtimes:
            self.reservations.append((movie.title, time))
            print(f"Rezerwacja na film '{movie.title}' o godzinie {time} została dodana.")
        else:
            print(f"Seans o godzinie {time} nie jest dostępny.")

    def display_reservations(self):
        """Wyświetla listę rezerwacji klienta."""
        print(f"Rezerwacje klienta {self.first_name} {self.last_name}:")
        if self.reservations:
            for movie_title, time in self.reservations:
                print(f"Film: {movie_title}, Godzina: {time}")
        else:
            print("Brak rezerwacji.")


class VIPCustomer(Customer):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def get_discounted_price(self, price):
        """Zwraca cenę biletu po zniżce 20%."""
        discounted_price = price * 0.8
        return discounted_price

    def book_private_show(self, movie, time):
        """Rezerwuje cały seans dla VIP-a."""
        print(f"VIP klient {self.first_name} {self.last_name} zarezerwował prywatny seans filmu '{movie.title}' o godzinie {time}.")


class Cinema:
    def __init__(self):
        self.movies = []
        self.customers = []

    def add_movie(self, movie):
        """Dodaje nowy film do repertuaru."""
        self.movies.append(movie)

    def add_customer(self, customer):
        """Dodaje nowego klienta."""
        self.customers.append(customer)

    def display_movies(self):
        """Wyświetla wszystkie filmy w repertuarze."""
        print("Dostępne filmy w repertuarze:")
        for movie in self.movies:
            movie.display_details()


def main():
    movie1 = Movie("Wielka Przygoda", 120, ["14:00", "17:00", "20:00"])
    movie2 = Movie("Nocny Patrol", 90, ["15:00", "18:00", "21:00"])

    customer1 = Customer("Jan", "Kowalski")
    vip_customer1 = VIPCustomer("Anna", "Nowak")

    cinema = Cinema()
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    cinema.add_customer(customer1)
    cinema.add_customer(vip_customer1)

    cinema.display_movies()

    customer1.add_reservation(movie1, "17:00")
    customer1.add_reservation(movie2, "18:00")

    vip_customer1.add_reservation(movie1, "20:00")
    price = 50  
    print(f"Cena biletu VIP z rabatem: {vip_customer1.get_discounted_price(price)} zł")

    vip_customer1.book_private_show(movie2, "21:00")

    customer1.display_reservations()
    vip_customer1.display_reservations()


if __name__ == "__main__":
    main()
