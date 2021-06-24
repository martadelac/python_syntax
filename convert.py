def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results.

    - unit_in: either "f" or "c" 
    - unit_out: either "f" or "c"
    - temp: temperature (in f or c, depending on unit_in)

    Return results of conversion, if any.

    If unit_in or unit_out are invalid, return "Invalid unit [UNIT_IN]".

    For example:

      convert_temp("c", "f", 0)  =>  32.0
      convert_temp("f", "c", 212) => 100.0

      FAHRENHEIT TO CELSIUS:
      Take the °F temperature and subtract 32. Multiply this number by 5. 
      Divide this number by 9 to obtain your answer in °C

      CELSIUS TO FAHRENHEIT
      Multiplica los grados Centígrados por 9/5.
      Súmale 32º para adaptar el equivalente en la escala Fahrenheit.
      Ejemplo: convierte 37º C a Fahrenheit. 37 * 9/5 = 333/5 = 66.6. 66.6 + 32 = 98.6o F.
    """
    # YOUR CODE HERE
def convert_temp(unit_in, unit_out, temp):

    if unit_in == "c" and unit_out == "f":
      temp = temp * (9/5) + 32

    if unit_in == "f" and unit_out=="c":
      temp = ((temp - 32) * 5)/9
    
    # if unit_in != "c" or "f":
    #   return f"Invalid unit {unit_in}"

    # if unit_out != "c" or "f":
    #   return f"Invalid unit {unit_out}"
  
    return temp

     
  



# print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
# print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
# print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
# print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
# print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

