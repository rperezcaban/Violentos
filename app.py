import streamlit as st
from streamlit_utils import num_check
from streamlit_utils import check_yes_no

#st.set_page_config(layout="wide")

parentesco = ["Abuel@", "Padre", "Madre", "Tí@", "Hij@", "Sobrin@", "Niet@", "Espos@", "Prim@", "Herman@", "Amig@"]
sorted_list = sorted(parentesco)
sorted_list.append("Otro")
# if "role" not in st.session_state:
#     st.session_state.role = None

st.header("Campamento Violentos")
with st.container(border=True):
    #col1, col2 = st.columns(2)
    #Informacion Personal Section
    st.subheader("Información Personal", divider=True)
    name = st.text_input("Nombre Completo", 
                        max_chars=200, 
                        key="name", 
                        type="default",
                        value=None,
                        placeholder="Provea su nombre completo",
                        help="Provea su nombre con ambos appellidos"
                        )

    age = st.number_input("Edad", min_value=18, max_value=100, value=None, step=1, key="age", placeholder="Favor de ingresar su edad")

    pnum = st.text_input("Número de Telefono", 
                        max_chars=10, 
                        key="pnumber", 
                        value=None, 
                        placeholder="Inserte número de teléfono", 
                        help="Inserte número de teléfono sin ningun símbolo"
                        )
    if pnum is not None and num_check(pnum) == False:
        st.error("Favor de ingresar solo números sin caracteres especiales")  

    email = st.text_input("Email",
                        max_chars=200,
                        key='email',
                        placeholder='Favor proveer su correo electrónico',
                        value=None
                        )

    condition = st.selectbox("Condición Médica?", 
                        options=["Si", "No"], 
                        index=None, 
                        key='condition', 
                        placeholder="Escoja 'Si' o 'No'"
                        )
    if condition == "Si":
        condition_name = st.text_input("Nombre de la condición o condiciones",
                        max_chars=200,
                        key='condition_name',
                        placeholder='Provea nombres',
                        value=None
                        )
    
    #Contact de Emergencia Section
    st.subheader("Contacto de Emergencia", divider=True)

    emName = st.text_input("Nombre Completo", 
                        max_chars=200, 
                        key="em_name",
                        value=None, 
                        type="default",
                        placeholder="Provea nombre del contact de emergencias",
                        help="Provea su nombre con ambos appellidos"
                        )

    emNum = st.text_input("Número de Telefono", 
                        max_chars=10, 
                        key="em_num", 
                        value=None, 
                        placeholder="Inserte número de teléfono", 
                        help="Inserte número de teléfono sin ningun símbolo"
                        )
    if emNum is not None and num_check(emNum) == False:
        st.error("Favor de ingresar solo números sin caracteres especiales")
        
    parentesco = st.selectbox("Parentesco", 
                            options=sorted_list, 
                            index=None, 
                            key='parentesco', 
                            placeholder="Provea el parentesco", 
                            help="Provea el parentesco con la persona de contacto"
                            )
    
    #Seccion General
    st.subheader("Información General", divider=True)

    iglesia = st.selectbox("Asiste a alguna iglesia?", 
                        options=["Si", "No"], 
                        index=None, 
                        key='iglesia', 
                        placeholder="Provea la iglesia a la que asiste"
                        )
    
    if iglesia == "Si":
        pastorsName = st.text_input("Nombre del Pastor",
                                    max_chars=200,
                                    value=None,
                                    key='pastor',
                                    placeholder="Provea el nombre del pastor",
                                    help="Provea el nombre del pastor de la iglesia a la que asiste"
                                    )
    
    expectative = st.text_area("Qué espera del campamento?",
                            value=None,
                            max_chars=250,
                            key="expectative",
                            placeholder="Qué esperas del campamento?"
                            )
    
    size = st.selectbox("Size de Camisa", 
                        options=["Small", "Medium", "Large", "X-Large", "1X-Large", "2X-Large"],
                        index=None,
                        key='size',
                        placeholder="Favor de seleccionar su talla",
                        help="""Las camisas corren al size. Esto significa que si usted es Medium regularmente,
                        la talla seleccionada debería ser su talla regular.
                        """                  
                        )
    
    # terms = st.checkbox("Acepto las reglas y terminos", value=False, key="terms")
    # st.page_link("pages/terminos.py", label="Home", icon="🏠")

    #Seccion de Reglas y Terminos
    st.subheader("Reglas y Terminos", divider=True)
    @st.experimental_dialog("Términos y Condiciones")
    def terms():
        st.markdown(unsafe_allow_html=True,
                            body="""

        Estos términos y condiciones ("Términos") rigen el uso del servicio proporcionado por [Nombre del Servicio] ("Nosotros", "Nuestro", "Nosotros"), accesible a través del sitio web [www.ejemplodeservicio.com] ("Sitio web"). Al utilizar nuestro servicio, usted ("Usuario", "Usted") acepta cumplir y estar sujeto a estos Términos. Si no está de acuerdo con alguna parte de los términos, no puede acceder al servicio.

        **Cuentas**

        Al registrarse para obtener una cuenta en nuestro servicio, usted acepta proporcionar información precisa, completa y actualizada sobre usted como se solicita en el formulario de registro. Usted es responsable de mantener la confidencialidad de su contraseña y es totalmente responsable de todas las actividades que ocurran bajo su cuenta. Usted acepta notificarnos inmediatamente de cualquier uso no autorizado de su cuenta o cualquier otra violación de seguridad. No seremos responsables por ninguna pérdida que pueda surgir de la divulgación no autorizada de su información de inicio de sesión.

        **Uso Aceptable**

        Usted acepta usar nuestro servicio solo para fines legales y de acuerdo con estos Términos. Usted acepta no utilizar nuestro servicio para:

        - Violar cualquier ley o regulación aplicable.
        - Realizar actividades fraudulentas, incluido el phishing o el fraude.
        - Recopilar información personal de otros usuarios.
        - Transmitir material que sea difamatorio, ofensivo, obsceno o de otro modo objetable.
        - Interferir con el funcionamiento normal de nuestro servicio.

        **Propiedad Intelectual**

        Nuestro servicio y su contenido, características y funcionalidad son y seguirán siendo propiedad exclusiva de [Nombre del Servicio]. El servicio está protegido por derechos de autor, marcas comerciales y otras leyes de los Estados Unidos y países extranjeros. Nuestros nombres comerciales y logotipos no pueden ser utilizados en relación con ningún producto o servicio sin el consentimiento previo por escrito de [Nombre del Servicio].

        **Limitación de Responsabilidad**

        En ningún caso [Nombre del Servicio], sus directores, empleados, socios o afiliados serán responsables ante usted por cualquier daño indirecto, incidental, especial, consecuente o punitivo que surja de o esté relacionado con su uso del servicio.

        **Cambios**

        Nos reservamos el derecho, a nuestra sola discreción, de modificar o reemplazar estos Términos en cualquier momento. Si una revisión es material, intentaremos proporcionar al menos 30 días de aviso antes de que los nuevos términos entren en vigencia. Lo que constituye un cambio material se determinará a nuestra sola discreción.

        **Contacto**

        Si tiene alguna pregunta sobre estos Términos, puede contactarnos en [correo electrónico de contacto].

        ---

        Recuerda que estos términos y condiciones son solo un ejemplo básico y pueden variar según el servicio y las leyes locales aplicables. Siempre es recomendable buscar asesoramiento legal para redactar términos y condiciones adecuados para tu servicio específico.

        """
        )
    if "terms" not in st.session_state:
        if st.button("Leer reglas y términos"):
            terms()
       
    accept = st.checkbox("Acepto los terminos", key='terms_accepted', value=True)

    if accept:
        submit = st.button(label="Submit", 
                        type="primary", 
                        use_container_width=True, 
                        key="submit"
                        )
        if submit:   
            for i in st.session_state:
                
                print("*************")
                print(i)
                print(st.session_state.get(i))
    else:
        st.warning("Para someter el formulario debe aceptar las reglas y terminos del campamento",icon="⚠")