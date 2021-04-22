class interface_pool_temp:
    def get_actual_temp(self) -> float:
        # Retourne la température actuelle
        pass

    def get_last_days_temp(self) -> list:
        # Retourne la liste des températures des 7 derniers jours
        pass

    def set_heater(self, active: bool) -> None:
        # Allume ou éteint le chauffage de la piscine en fonction du booléen
        pass
