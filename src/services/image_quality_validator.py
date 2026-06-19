from PIL import Image


class ImageQualityValidator:

    MIN_WIDTH = 300
    MIN_HEIGHT = 300

    def validate(self, image_paths):

        results = []

        for image_path in image_paths:

            try:
                image = Image.open(image_path)

                width, height = image.size

                issues = []

                if width < self.MIN_WIDTH:
                    issues.append("Image width too small.")

                if height < self.MIN_HEIGHT:
                    issues.append("Image height too small.")

                valid = len(issues) == 0

                results.append({
                    "image": image_path,
                    "valid": valid,
                    "width": width,
                    "height": height,
                    "issues": issues,
                })

            except Exception as e:

                results.append({
                    "image": image_path,
                    "valid": False,
                    "width": 0,
                    "height": 0,
                    "issues": [str(e)],
                })

        return results