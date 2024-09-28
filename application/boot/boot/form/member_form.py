from boot.model.member import Member
from pweb_form_rest import fields, PWebForm


class MemberDetailsForm(PWebForm):

    class Meta:
        model = Member
        load_instance = True

    name = fields.String(required=True, error_messages={"required": "Please enter name"})
    roll = fields.String(required=True, error_messages={"required": "Please enter roll"})
    registration = fields.String(required=True, error_messages={"required": "Please enter registration"})
    email = fields.Email(required=True, error_messages={"required": "Please enter email"})
    address = fields.String(allow_none=True, type="textarea")


class MemberCreateForm(MemberDetailsForm):
    class Meta:
        model = Member
        load_instance = True

    password = fields.String(required=True, error_messages={"required": "Please enter password"}, type="password")


class MemberUpdateForm(MemberDetailsForm):
    class Meta:
        model = Member
        load_instance = True

    id = fields.Integer(required=True, error_messages={"required": "Please enter id"}, type="hidden", isLabel=False)