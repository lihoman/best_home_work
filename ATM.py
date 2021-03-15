def get_all_money(dict_with_greenbacks):
    """Finding how much money in my ATM"""
    all_money = sum(map(lambda x: x[0] * x[1], dict_with_greenbacks.items()))
    return all_money


class ATM:

    def __init__(self, dict_with_greenbacks_in_ATM):
        self.available_greenbacks_in_ATM = dict_with_greenbacks_in_ATM  # dict with number of every greenback in ATM
        self.greenbacks_for_client = {  # empty dict with greenbacks before expunging money from ATM
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
        }

    def withdraw_money(self):
        """Func which call another func if the amount is less then exist in ATM"""
        cash_to_withdraw = self.correct_input()
        all_money_in_ATM = get_all_money(self.available_greenbacks_in_ATM)
        # Compare client amount with available amount of money in ATM
        if cash_to_withdraw > all_money_in_ATM:
            return f'Not enough money in ATM. Available amount: {all_money_in_ATM}'
        else:
            return self.give_money_to_client(cash_to_withdraw)

    def correct_input(self):
        """To correct number of amount from clients input"""
        input_cash = input("Enter the amount you want to cash out: ")
        try:
            int(input_cash)
        except ValueError:
            print('Please, enter a number in correct form!')
            self.correct_input()
        else:
            return int(input_cash)

    def give_money_to_client(self, cash_to_withdraw):
        """Return answer depending on exists or no kind of greenbacks for amount to cash out"""
        # Compare then amount which want to cash out client will be exist in greenbacks from ATM
        self.money_available_to_client(cash_to_withdraw)  # the main function which does all operations with ATM
        available_cash_for_client = get_all_money(self.greenbacks_for_client)  # available amount in greenbacks in ATM
        if cash_to_withdraw <= available_cash_for_client:
            return self.answer_to_client()
        else:
            return f'Not enough greenbacks. Money available to cash out: {available_cash_for_client}'

    def money_available_to_client(self, cash_to_withdraw_alterable):
        """Changing dictionaries with money in ATM and money for client after cash out"""
        for key in self.available_greenbacks_in_ATM:
            while cash_to_withdraw_alterable >= key and self.available_greenbacks_in_ATM[key] > 0:
                cash_to_withdraw_alterable -= key  # to subtraction one greenback from amount to cash out
                self.greenbacks_for_client[key] += 1  # addition this greenback to dict with greenbacks for client
                self.available_greenbacks_in_ATM[key] -= 1  # subtraction this greenback from ATM

    def answer_to_client(self):
        """Do answer what greenbacks client will have"""
        answer = f'Please, take your cash in next greenbacks:\n'
        for key, value in self.greenbacks_for_client.items():
            if value != 0:
                answer += f'{key} rub: {value}\n'  # if greenback exist => add in finish answer
        return answer
