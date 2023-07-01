from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    text: str

    def set_text(self, text: str):
        self.text = text


@pc.route(route="/", title="나의 투자 성향은?")
def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("나의 투자 성향에 대해 알아보아요!", font_size="5em"),
            pc.input(
                on_change=State.set_text,
                placeholder="이름을 입력해주세요.",
                width="30%",
            ),
            pc.link(
                pc.button(
                    "시작!",
                    background_color="green",
                    size="lg",
                ),
                href="/go",
                button=True,
            ),
            spacing="3em",
        ),
        background_image="/bonobono.jpg",
        background_position="center",
        background_size="cover",
        background_repeat="no-repeat",
        height="100vh",
    )


@pc.route(route="/go", title="시작")
def start() -> pc.Component:
    name = State.text
    return pc.vstack(
        pc.text(f"{name}님, 환영합니다.", font_size="5em"),
    )


app = pc.App(state=State)
app.compile()
