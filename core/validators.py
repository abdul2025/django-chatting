from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


_NAME_REGEX = RegexValidator(
    regex=r"^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z]+[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]*$", message=_("Special characters and digits are now allowed."),
)

_COLLEGE_REGEX = RegexValidator(
    regex=r"^[\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z]+[\-\&\u0600-\u065F\u066A-\u06EF\u06FA-\u06FFa-zA-Z ]*$", message=_("Digits and special characters (except & and -) are now allowed."),
)

_CARD_HOLDER_NAME_REGEX = RegexValidator(
    regex=r"^((?:[A-Za-z]+ ?){1,6})$", message=_("Special characters and digits are now allowed."),
)

_PHONE_REGEX = RegexValidator(
    regex=r"^+\d{18}$", message=_("Mobile number must be 18 digits starting with '+'."),
)


_ID_NUMBER_REGEX = RegexValidator(
    regex=r"\d{10}$", message=_("ID number must be 10 digits."),
)

_CR_NUMBER_REGEX = RegexValidator(
    regex=r"\d{10}$", message=_("Commercial register number must be 10 digits."),
)

_VAT_NUMBER_REGEX = RegexValidator(
    regex=r"\d{15}$", message=_("VAT number must be 15 digits."),
)

_IBAN_REGEX = RegexValidator(
    regex=r"^SA\s*(?:\S\s*){22}$", message=_("IBAN must be in a form of 'SA' followed with 22 digits."),
)
