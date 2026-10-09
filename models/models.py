from . import db

plantas_referencias = db.Table(
    "plantas_referencias",

    db.Column(
        "planta_id",
        db.BigInteger,
        db.ForeignKey("plantas.id", ondelete="CASCADE"),
        primary_key=True
    ),

    db.Column(
        "referencia_id",
        db.BigInteger,
        db.ForeignKey("referencias.id", ondelete="CASCADE"),
        primary_key=True
    )
)


class Planta(db.Model):
    __tablename__ = "plantas"

    id = db.Column(db.BigInteger, primary_key=True)
    nome_cientifico = db.Column(db.String(255), nullable=False, index=True)
    nome_popular = db.Column(db.String(255), nullable=False, index=True)
    familia_botanica = db.Column(db.String(255))
    parte_utilizada = db.Column(db.Text)
    descricao = db.Column(db.Text)
    criado_em = db.Column(db.DateTime)
    atualizado_em = db.Column(db.DateTime)

    indicacoes = db.relationship("Indicacao", back_populates="planta", cascade="all, delete-orphan")
    contraindicacoes = db.relationship("Contraindicacao", back_populates="planta", cascade="all, delete-orphan")
    precaucoes = db.relationship("Precaucao", back_populates="planta", cascade="all, delete-orphan")
    efeitos_adversos = db.relationship("EfeitoAdverso", back_populates="planta", cascade="all, delete-orphan")
    interacoes = db.relationship("InteracaoMedicamentosa", back_populates="planta", cascade="all, delete-orphan")
    formas = db.relationship("FormaFarmaceutica", back_populates="planta", cascade="all, delete-orphan")
    formulas = db.relationship("Formula", back_populates="planta", cascade="all, delete-orphan", order_by="Formula.numero_formula")
    tempos_utilizacao = db.relationship("TempoUtilizacao", back_populates="planta", cascade="all, delete-orphan")
    superdosagens = db.relationship("Superdosagem", back_populates="planta", cascade="all, delete-orphan")
    prescricoes = db.relationship("Prescricao", back_populates="planta", cascade="all, delete-orphan")
    armazenamentos = db.relationship("Armazenamento", back_populates="planta", cascade="all, delete-orphan")
    advertencias = db.relationship("AdvertenciaFormulacao", back_populates="planta", cascade="all, delete-orphan")
    observacoes_fonte = db.relationship("ObservacaoFonte", back_populates="planta", cascade="all, delete-orphan")
    referencias = db.relationship("Referencia", secondary=plantas_referencias, back_populates="plantas")
    referencias = db.relationship("Referencia", secondary=plantas_referencias, back_populates="plantas")

class Indicacao(db.Model):
    __tablename__ = "indicacoes"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    indicacao = db.Column(db.Text, nullable=False)
    planta = db.relationship("Planta", back_populates="indicacoes")


class Contraindicacao(db.Model):
    __tablename__ = "contraindicacoes"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    contraindicacao = db.Column(db.Text, nullable=False)
    planta = db.relationship("Planta", back_populates="contraindicacoes")


class Precaucao(db.Model):
    __tablename__ = "precaucoes"

    id = db.Column(db.BigInteger, primary_key=True)

    planta_id = db.Column(
        db.BigInteger,
        db.ForeignKey("plantas.id", ondelete="CASCADE"),
        nullable=False
    )

    precaucao = db.Column(
        db.Text,
        nullable=False
    )

    planta = db.relationship(
        "Planta",
        back_populates="precaucoes"
    )


class EfeitoAdverso(db.Model):
    __tablename__ = "efeitos_adversos"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    planta_id = db.Column(
        db.BigInteger,
        db.ForeignKey("plantas.id", ondelete="CASCADE"),
        nullable=False
    )

    efeito_adverso = db.Column(
        db.Text,
        nullable=False
    )

    planta = db.relationship(
        "Planta",
        back_populates="efeitos_adversos"
    )


class InteracaoMedicamentosa(db.Model):
    __tablename__ = "interacoes_medicamentosas"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    medicamento = db.Column(db.String(255))
    interacao = db.Column(db.Text, nullable=False)
    planta = db.relationship("Planta", back_populates="interacoes")


class FormaFarmaceutica(db.Model):
    __tablename__ = "formas_farmaceuticas"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    forma = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text)
    planta = db.relationship("Planta", back_populates="formas")


class Formula(db.Model):
    __tablename__ = "formulas"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    numero_formula = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(255))
    descricao = db.Column(db.Text)

    planta = db.relationship("Planta", back_populates="formulas")
    preparos = db.relationship("Preparo", back_populates="formula", cascade="all, delete-orphan")
    posologias = db.relationship("Posologia", back_populates="formula", cascade="all, delete-orphan")
    advertencias = db.relationship("AdvertenciaFormulacao", back_populates="formula")


class Preparo(db.Model):
    __tablename__ = "preparos"
    id = db.Column(db.BigInteger, primary_key=True)
    formula_id = db.Column(db.BigInteger, db.ForeignKey("formulas.id", ondelete="CASCADE"), nullable=False)
    metodo = db.Column(db.String(100))
    tempo_preparo_minutos = db.Column(db.Integer)
    materia_prima = db.Column(db.Text)
    proporcao = db.Column(db.Text)
    descricao = db.Column(db.Text)
    formula = db.relationship("Formula", back_populates="preparos")


class Posologia(db.Model):
    __tablename__ = "posologias"
    id = db.Column(db.BigInteger, primary_key=True)
    formula_id = db.Column(db.BigInteger, db.ForeignKey("formulas.id", ondelete="CASCADE"), nullable=False)
    via_administracao = db.Column(db.String(100), nullable=False)
    dose = db.Column(db.Text)
    frequencia = db.Column(db.Text)
    intervalo = db.Column(db.Text)
    quantidade_diaria_min = db.Column(db.Numeric(10, 2))
    quantidade_diaria_max = db.Column(db.Numeric(10, 2))
    unidade = db.Column(db.String(50))
    observacoes = db.Column(db.Text)
    formula = db.relationship("Formula", back_populates="posologias")


class TempoUtilizacao(db.Model):
    __tablename__ = "tempos_utilizacao"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    tempo_maximo = db.Column(db.Text)
    orientacao = db.Column(db.Text)
    planta = db.relationship("Planta", back_populates="tempos_utilizacao")


class Superdosagem(db.Model):
    __tablename__ = "superdosagem"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    conduta = db.Column(db.Text)
    planta = db.relationship("Planta", back_populates="superdosagens")


class Prescricao(db.Model):
    __tablename__ = "prescricoes"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    status = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    planta = db.relationship("Planta", back_populates="prescricoes")


class Armazenamento(db.Model):
    __tablename__ = "armazenamento"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    embalagem = db.Column(db.Text)
    protecao = db.Column(db.Text)
    armazenamento = db.Column(db.Text)
    observacoes = db.Column(db.Text)
    planta = db.relationship("Planta", back_populates="armazenamentos")


class AdvertenciaFormulacao(db.Model):
    __tablename__ = "advertencias_formulacao"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    formula_id = db.Column(db.BigInteger, db.ForeignKey("formulas.id", ondelete="CASCADE"))
    advertencia = db.Column(db.Text, nullable=False)
    planta = db.relationship("Planta", back_populates="advertencias")
    formula = db.relationship("Formula", back_populates="advertencias")


class ObservacaoFonte(db.Model):
    __tablename__ = "observacoes_fonte"
    id = db.Column(db.BigInteger, primary_key=True)
    planta_id = db.Column(db.BigInteger, db.ForeignKey("plantas.id", ondelete="CASCADE"), nullable=False)
    categoria = db.Column(db.String(100))
    observacao = db.Column(db.Text, nullable=False)
    planta = db.relationship("Planta", back_populates="observacoes_fonte")


class Referencia(db.Model):
    __tablename__ = "referencias"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    titulo = db.Column(
        db.Text,
        nullable=False
    )

    autores = db.Column(
        db.Text
    )

    instituicao = db.Column(
        db.String(255)
    )

    ano = db.Column(
        db.SmallInteger
    )

    tipo_fonte = db.Column(
        db.String(100)
    )

    url = db.Column(
        db.Text
    )

    doi = db.Column(
        db.String(255)
    )

    referencia_formatada = db.Column(
        db.Text
    )

    observacoes = db.Column(
        db.Text
    )

    criado_em = db.Column(
        db.DateTime
    )

    plantas = db.relationship(
        "Planta",
        secondary=plantas_referencias,
        back_populates="referencias"
    )