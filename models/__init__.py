from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .models import (
    Planta,
    Indicacao,
    Contraindicacao,
    Precaucao,
    InteracaoMedicamentosa,
    FormaFarmaceutica,
    Formula,
    Preparo,
    Posologia,
    TempoUtilizacao,
    Superdosagem,
    Prescricao,
    Armazenamento,
    AdvertenciaFormulacao,
    ObservacaoFonte,
)
