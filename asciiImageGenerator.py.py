from PIL import Image

class asciiImageGenerator:

    ASCII_CHARACTERS = ' _.,-=+:;cba!?0123456789$W#@Ñ'

    def resizeImage(self, image, newWidth):

        width, height = image.size

        aspectRatio = height / width

        newHeight = int(newWidth * aspectRatio * 0.43)
        resizedImage = image.resize((newWidth, newHeight))

        return resizedImage

    def readImage(self, image):

        img = image.convert("L")
        pixels = img.getdata()

        return list(pixels)

    def displayAsciiImage(self, path: str, newWidth=110):

        image = self.resizeImage(image=Image.open(path), newWidth=newWidth)

        pixels = self.readImage(image=image)
        pixelCount = len(pixels)

        characters = "".join([self.ASCII_CHARACTERS[pixel // 30] for pixel in pixels])

        charImage = "\n".join(characters[i : (i + newWidth)] for i in range(0, pixelCount, newWidth))

        return charImage


if __name__ == "__main__":

    path = "K:\\Images\\t247675504.jpg"

    gen = asciiImageGenerator()
    asciiImage = gen.displayAsciiImage(path=path)

    print(asciiImage)
