def format_name(l_name, f_name):
   formated_l_name = l_name.title()
   formated_f_name = f_name.title()
   return f"{formated_l_name}, {formated_f_name}"

formated_names = format_name("AdOneg", "VioLet")
print(formated_names)