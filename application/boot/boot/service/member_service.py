from pweb import url_for
from boot.form.member_form import MemberCreateForm, MemberUpdateForm, MemberDetailsForm
from boot.model.member import Member
from pweb_form_rest.crud.pweb_form_data_crud import FormDataCRUD


class MemberService:
    form_data_crud = FormDataCRUD(model=Member)

    def create(self):
        params = {"button": "Create", "action": url_for("member_controller.create")}
        form = MemberCreateForm()
        return self.form_data_crud.create(view_name="member/form", form=form, redirect_url=url_for("member_controller.list"), params=params)

    def update(self, model_id: int):
        params = {"button": "Update", "action": url_for("member_controller.update", id=model_id)}
        form = MemberUpdateForm()
        return self.form_data_crud.update(view_name="member/form", model_id=model_id, update_form=form, redirect_url=url_for("member_controller.list"), params=params)

    def details(self, model_id: int):
        form = MemberDetailsForm()
        return self.form_data_crud.details("member/details", model_id=model_id, redirect_url=url_for("member_controller.list"), display_from=form)

    def delete(self, model_id: int):
        return self.form_data_crud.delete(model_id=model_id, redirect_url=url_for("member_controller.list"))

    def list(self):
        search_fields = ["name", "email"]
        return self.form_data_crud.paginated_list(view_name="member/list", search_fields=search_fields)