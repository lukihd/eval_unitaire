from exercice_4_inteface import interface_pool_temp


class pool_temp(interface_pool_temp):
    def __init__(self, pool_logic=interface_pool_temp):
        self.heater = False
        self.pool_logic = pool_logic

    def enable_heater(self):
        if sum(self.pool_logic.get_last_days_temp(self)) / len(self.pool_logic.get_last_days_temp(self)) >= 20 and self.pool_logic.get_actual_temp(self) >= 25:
            self.pool_logic.set_heater(self, active=True)
        else:
            self.pool_logic.set_heater(self, active=False)
