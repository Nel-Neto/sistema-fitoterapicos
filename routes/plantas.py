from flask import Blueprint, render_template, request, abort
from sqlalchemy import or_
from sqlalchemy.orm import selectinload
from models import db, Planta, Indicacao, Formula, InteracaoMedicamentosa

plantas_bp = Blueprint("plantas", __name__)


@plantas_bp.route("/")
def index():
    destaques = db.session.execute(
        db.select(Planta).order_by(Planta.nome_popular).limit(6)
    ).scalars().all()
    total = db.session.scalar(db.select(db.func.count(Planta.id)))
    return render_template("index.html", plantas=destaques, total=total)


@plantas_bp.route("/plantas")
def listar_plantas():
    plantas = db.session.execute(
        db.select(Planta).order_by(Planta.nome_popular)
    ).scalars().all()
    return render_template("plantas.html", plantas=plantas)


@plantas_bp.route("/plantas/<int:planta_id>")
def detalhes_planta(planta_id):
    stmt = (
        db.select(Planta)
        .where(Planta.id == planta_id)
        .options(
            selectinload(Planta.indicacoes),
            selectinload(Planta.contraindicacoes),
            selectinload(Planta.precaucoes),
            selectinload(Planta.efeitos_adversos),
            selectinload(Planta.interacoes),
            selectinload(Planta.formas),
            selectinload(Planta.formulas).selectinload(Formula.preparos),
            selectinload(Planta.formulas).selectinload(Formula.posologias),
            selectinload(Planta.tempos_utilizacao),
            selectinload(Planta.superdosagens),
            selectinload(Planta.prescricoes),
            selectinload(Planta.armazenamentos),
            selectinload(Planta.advertencias),
            selectinload(Planta.observacoes_fonte),
            selectinload(Planta.referencias),
        )
    )
    planta = db.session.execute(stmt).scalar_one_or_none()
    if not planta:
        abort(404)
    return render_template("detalhes_planta.html", planta=planta)


@plantas_bp.route("/buscar")
def buscar():
    termo = request.args.get("q", "").strip()

    if not termo:
        return render_template("busca.html", termo="", plantas=[])

    padrao = f"%{termo}%"
    stmt = (
        db.select(Planta)
        .outerjoin(Indicacao)
        .where(
            or_(
                Planta.nome_popular.ilike(padrao),
                Planta.nome_cientifico.ilike(padrao),
                Planta.familia_botanica.ilike(padrao),
                Indicacao.indicacao.ilike(padrao),
            )
        )
        .distinct()
        .order_by(Planta.nome_popular)
    )

    plantas = db.session.execute(stmt).scalars().all()
    return render_template("busca.html", termo=termo, plantas=plantas)

@plantas_bp.route("/interacoes")
def buscar_interacoes():
    termo = request.args.get("q", "").strip()

    resultados = []

    if termo:
        padrao = f"%{termo}%"

        stmt = (
            db.select(InteracaoMedicamentosa)
            .join(InteracaoMedicamentosa.planta)
            .where(
                or_(
                    Planta.nome_popular.ilike(padrao),
                    Planta.nome_cientifico.ilike(padrao),
                    InteracaoMedicamentosa.medicamento.ilike(padrao),
                )
            )
            .options(
                selectinload(InteracaoMedicamentosa.planta)
            )
            .order_by(
                Planta.nome_popular,
                InteracaoMedicamentosa.medicamento
            )
        )

        resultados = db.session.execute(stmt).scalars().all()

    return render_template(
        "interacoes.html",
        termo=termo,
        resultados=resultados
    )
