import argparse, math, sys
from PIL import Image

end_chars_base = [1, 1, 1, 1, 1, 1, 1, 1]

def get_binary(x):
	return bin(x)[2:].zfill(8)

def change_lsb(byte, new):
	return byte[:-1] + str(new)

def change_color(color_base, bit):
	binary_color = get_binary(color_base)
	color_updated = change_lsb(binary_color, bit)
	return int(color_updated, 2)

def all_bits(text):
	list_all_bits = []
	for char in text:
		in_ascii = ord(char)
		in_binary = get_binary(in_ascii)
		for bit in in_binary:
			list_all_bits.append(bit)
	for bit in end_chars_base:
		list_all_bits.append(bit)
	return list_all_bits

def start(message, image_input):
	print("Iniciando...".format(message))
	image = Image.open(image_input)
	pixels = image.load()

	image_size = image.size
	image_x = image_size[0]
	image_y = image_size[1]

	list_all_bits = all_bits(message)
	bit_write_count = 0
	image_length = len(list_all_bits)

	for x in range(image_x):
		for y in range(image_y):
			if bit_write_count < image_length:
				pixel = pixels[x, y]

				base_r = pixel[0]
				base_g = pixel[1]
				base_b = pixel[2]

				if bit_write_count < image_length:
					color_r_updated = change_color(base_r, list_all_bits[bit_write_count])
					bit_write_count += 1
				else:
					color_r_updated = base_r

				if bit_write_count < image_length:
					color_g_updated = change_color(base_g, list_all_bits[bit_write_count])
					bit_write_count += 1
				else:
					color_g_updated = base_g

				if bit_write_count < image_length:
					color_b_updated = change_color(base_b, list_all_bits[bit_write_count])
					bit_write_count += 1
				else:
					color_b_updated = base_b

				pixels[x, y] = (color_r_updated, color_g_updated, color_b_updated)
			else:
				break
		else:
			continue
		break

	if bit_write_count >= image_length:
		print("El texto fue escrito correctamente!")
	else:
		print("Por favor ingresa una imagen de mayor tamaño.")
	image.save('output_'+image_input)

if __name__ == '__main__':
	print('Tool orientada a ocultar texto en una Imagen')
	print('Desarrollado solo con fines orientativos y conceptuales')
	print('Developed by @SixP4ck3r')
	print('')
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--text", help='Texto de entrada a ocultar', required=True)
	parser.add_argument("-i", "--image", help='Archivo de entrada Imagen PNG', required=True)
	args = parser.parse_args()
	
	start(args.text, args.image)