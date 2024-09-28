from boot.service.member_service import MemberService
from pweb import Blueprint

member_url_prefix = "/member"
member_controller = Blueprint(
    "member_controller",
    __name__,
    url_prefix=member_url_prefix
)
member_service = MemberService()


@member_controller.route("/create", methods=['POST', 'GET'])
def create():
    return member_service.create()


@member_controller.route("/details/<int:id>", methods=['GET'])
def details(id: int):
    return member_service.details(id)


@member_controller.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id: int = None):
    return member_service.update(id)


@person_controller.route("/delete/<int:id>", methods=['GET'])
def delete(id: int):
    return person_service.delete(id)


@person_controller.route("/", methods=['GET'])
@person_controller.route("/list", methods=['GET'])
def list():
    return person_service.list()