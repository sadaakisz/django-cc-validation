import re

from django.db import models

# Create your models here.
class Card(models.Model):
    number = models.CharField(("number"), max_length=23)
    expires = models.DateField(("expiry date"))
    name = models.CharField(("associated name"), max_length=100)
    cvv = models.IntegerField(("security code"))

    def __str__(self):
        return self.number

    def valid_card(self):
        # https://stackoverflow.com/a/17337613
        plain_str = re.sub('[^0-9]', '', self.number)
        verification_digit = int(plain_str[-1])
        rev_str = "".join(reversed(plain_str))
        # 1 offset because of the verification digit
        even_pos_digits = [int(rev_str[i]) for i in range(len(rev_str)) if int(i)%2==1]
        odd_pos_digits = [int(rev_str[i]) for i in range(len(rev_str)) if int(i)%2==0 and i!=0]

        processed_even_digits = [1+(2*x)%10 if 2*x>=10 else 2*x for x in even_pos_digits]

        return (sum(processed_even_digits) + sum(odd_pos_digits) + verification_digit) % 10 == 0

    def issuing_network(self):
        # TODO: Implement remaining network checks
        if self.number.startswith("34") or self.number.startswith("37"):
            return "American Express"
        elif self.number.startswith("4"):
            return "Visa"
        else:
            return "Other"