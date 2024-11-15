class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12:   #correctly
            return 50
        elif 13 <= age <= 20: #correctly
            return 100
        elif 21 <= age <= 60: #correctly
            return 150
        elif age > 60: #correctly
            return 100
        

if __name__ == "__main__":
    zoo = Zoo()
    print(zoo.get_ticket_price(-5))
