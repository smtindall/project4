from parse_utils import parse_date

fname_personal = 'personal_info.csv'
fname_employment = 'employment.csv'
fname_update = 'update_status.csv'
fname_vehicles = 'vehicles.csv'
fnames = fname_personal,fname_employment,fname_update,fname_vehicles

personal_parser = (str,str,str,str,str)
employment_parser = (str,str,str,str)
vehicle_parser = (str,str,str,int)
update_parser = (str, parse_date, parse_date)
parsers = personal_parser,employment_parser, update_parser, vehicle_parser

personal_class_name = 'Personal'
employment_class_name = 'Employment'
vehicle_class_name = 'Vehicle'
update_class_name = 'UpdateStatus'
class_names = personal_class_name,employment_class_name,update_class_name, vehicle_class_name

personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True,True,False]
vehicle_fields_compress = [False, True, True, True]
update_fields_compress = [False, True, True]
compress_fields = (personal_fields_compress, employment_fields_compress,
                   update_fields_compress, vehicle_fields_compress)

