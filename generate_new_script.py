from openai import OpenAI
client = OpenAI()

def new_script(transcripts):
    template = "Write an script for someone read in a Instagram Reel about the new 'Campamento'. \n\nWrite the script in Spanish. \n\nDescripcion del Campamento: Campamento de Verano Vamos Alto 2024\n¡Únete a nosotros para una experiencia de verano inolvidable en el Campamento de Verano Vamos Alto 2024 del 22 al 27 de julio! Transforma tus vacaciones en un increíble viaje de ciencia y tecnología. Descubre tus talentos y habilidades, experimenta con la ciencia, aprende sobre robótica y finanzas personales, y explora tu creatividad en un entorno divertido y atractivo.\nDetalles del evento:\nFecha: 22-27 de julio\nEdades:12 a 16 años\nLugar: Auditorio Municipal de Apodaca, Gral. Ignacio Zaragoza S/N, Cabecera Municipal (Apodaca)\nFecha límite de registro: 18 de julio (Preferencia de inscripción para alumnos Vamos Alto y residentes de Apodaca)\nEnlace de registro: bit.ly/CampVA24\nActividades incluyen:\nExperimentos Científicos\nTalleres de Robótica\nLecciones de Finanzas Personales\nArte y Manualidades Creativas\nPara más información, contáctanos en vamosalto@apodaca.gob.mx o por WhatsApp al 8117986645. ¡No pierdas la oportunidad de enriquecer tu verano con aprendizaje y diversión! \n\nTo write the script, use the same style, tone and way of talking as in the scripts below. \n\nScripts:"
    
    for idx, transcript in enumerate(transcripts):
        template += f"\n\nScript {idx}: {transcript}"
    
    script = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful marketing assistant designed to output JSON."},
        {"role": "user", "content": template}
    ]
    )
    
    return script.choices[0].message.content

if __name__ == '__main__':
    t1 = "Sigue la crisis del agua en Nuevo León y ahorita en tu hogar hay de 3 sopas, o no te sale agua que en ese caso lo que tienes que hacer es esperar, ya se ha restablecido el servicio en la mayoría de los sectores de la ciudad y seguramente pronto también los será en el tuyo. La otra es que te esté saliendo el agua muy turbia, en este caso la puedes usar para higiene básica del hogar, pero no te bañes con ella, ni mucho menos laves los trastes, la usas para cocinar o para tomar. La otra opción es que ya te esté saliendo el agua clara, en este caso ya la puedes usar para lavar los trastes, para bañarte, para otras cuestiones de higiene, pero no la puedes consumir, no la tomes ni la usas para hacer comida, algo que si puedes hacer es esa agua que sale la pones a hervir, de esta manera eliminas los microorganismos y las bacterias y ya te la puedes tomar y usar para cocinar. Entonces estas son las 3 opciones en las que te puedes encontrar y que es lo que los expertos recomiendan que hagas, ayúdame a compartir esta información importante, aquí te seguiré informando de las cuestiones más relevantes que suceden con la crisis del agua en Nuevo León, ¡ánimo! y aquí estamos a la orden."
    t2 = "Muchas áreas de nuestra ciudad han estado teniendo problemas con el suministro de agua. Algunas tienen muy baja presión o de plano no tienen agua. Y esto se debe a fallas generalizadas en la infraestructura de agua y drenaje. Ahora que pasó la tormenta Alberto, si bien llenó las presas, también causó muchos daños, principalmente eléctricos, en la infraestructura de agua y drenaje. Ahorita están trabajando para resolverlos y se espera que el servicio se restablezca en las próximas horas. Pero estén tranquilos, obviamente no es un tema de desabasto de agua, más con la llegada de esta tormenta, sino algo pasajero, pero generalizado por las fallas que ha habido en la infraestructura. Aquí lo seguiré informando. ¡Ánimo!"
    t3 = "Este es el río Pesquería, va muy cargado porque se arreciaron mucho las lluvias en la madrugada y en lo que va del día, ahorita ya se calmaron un poco, el río Pesquería va como al 70% más o menos todavía no hay riesgo de que se desborde, déjenme les enseño del otro lado. Aquí cruzamos la calle con mucho cuidado, estamos en Santa Rosa, el Paseo de Santa Rosa donde preguntas es por allá, por donde está el otro puente, sin embargo vean lo cargado que va el río. Así estamos revisando los diferentes cauces de la ciudad, los más importantes, ninguno muestra al momento riesgos de que se vayan a desbordar. Sigamos cuidándonos, ay hijo de su... se entro en un transformado. Sigámonos cuidándonos les decía, tenemos que informarnos con las fuentes oficiales. El gobierno del estado anunció que el toque de queda se extendió hasta mañana a las 6 de la mañana sin embargo si hay transporte público. Manténgase en casa seguros, aquí los seguiré informando. ¡Ánimo!"
    transcripts = [t1, t2, t3]
    script = new_script(transcripts)
    print(script)
