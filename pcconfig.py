import pynecone as pc

class InvestingdiagnosisConfig(pc.Config):
    pass

config = InvestingdiagnosisConfig(
    app_name="investing_diagnosis",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)