from bd import db
from flask import Blueprint, request, session , redirect ,  render_template, jsonify
from Model.validar import validar
from Model.registro import registross

routes_validar= Blueprint("routes_validar", __name__)



# @routes_validar.route("/login", methods=["POST"])
# def login():
#     Ndocumento = request.json["Ndocumento"]
#     contraseña = request.json["contraseña"]
#     verificacion = db.session.query(validar).filter(validar.Ndocumento == Ndocumento, validar.contraseña == contraseña).first()

#     if verificacion:
#         session['admin_id'] = verificacion.id
#         return redirect("/")
#     else:
#         return "Credenciales inválidas"


# @routes_validar.route("/aprendices")
# def mostrar_aprendices():
#     admin_id = session.get('admin_id')
#     if admin_id:
#         # Obtener los aprendices correspondientes al administrador
#         aprendices = registross.query.filter_by(admin_id=admin_id).all()
#         return render_template("/menu", aprendices=aprendices)
#     else:
#         return "Acceso no autorizado"





@routes_validar.route("/login", methods=["POST"])
def login():
  
    Ndocumento = request.json["Ndocumento"]
    contraseña = request.json["contraseña"]
    verificacion = db.session.query(validar).filter(validar.Ndocumento == Ndocumento,validar.contraseña == contraseña,).first()

    if verificacion:
        session['admin_id'] = verificacion.id
        session['Ndocumento'] = verificacion.Ndocumento
        session['Nombre'] = verificacion.Nombre
        return "a"
    
@routes_validar.route('/obtener_datos_sesion')
def obtener_datos_sesion():
    admin_id = session.get('admin_id')
    Ndocumento = session.get('Ndocumento')
    Nombre = session.get('Nombre')
    return jsonify({'adminId': admin_id, 'Ndocumento': Ndocumento, 'Nombre': Nombre})