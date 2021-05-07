import argparse, math, sys
from PIL import Image

end_chars_base = '11111111'

def binary_to_decimal(binary):
	return int(binary, 2)

def get_lsb(byte):
	return byte[-1]

def get_binary(number):
	return bin(number)[2:].zfill(8)

def start(image):
	imagen = Image.open(image)
	pixels = imagen.load()

	image_size = imagen.size
	image_x = image_size[0]
	image_y = image_size[1]

	byte = ""
	hidden_data = ""

	for x in range(image_x):
		for y in range(image_y):
			pixel = pixels[x, y]

			base_r = pixel[0]
			base_g = pixel[1]
			base_b = pixel[2]

			byte += get_lsb(get_binary(base_r))
			if len(byte) >= 8:
				if byte == end_chars_base:
					break
				hidden_data += chr(binary_to_decimal(byte))
				byte = ""

			byte += get_lsb(get_binary(base_g))
			if len(byte) >= 8:
				if byte == end_chars_base:
					break
				hidden_data += chr(binary_to_decimal(byte))
				byte = ""

			byte += get_lsb(get_binary(base_b))
			if len(byte) >= 8:
				if byte == end_chars_base:
					break
				hidden_data += chr(binary_to_decimal(byte))
				byte = ""

		else:
			continue
		break
	print(f'El texto recuperado es: {hidden_data}')

if __name__ == '__main__':
	print('Tool orientada a recuperar el texto ocultado en una Imagen')
	print('Desarrollado solo con fines orientativos y conceptuales')
	print('Developed by @SixP4ck3r')
	print('')
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--image", help='Archivo de entrada Imagen PNG', required=True)
	args = parser.parse_args()
	
	start(args.image)