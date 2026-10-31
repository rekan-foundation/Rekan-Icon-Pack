# Rekan Icon Pack

A free collection of icons and stock footage provided by Rekan Foundation for nonprofit organizations, social impact institutions, content creators, designers, and developers.

Feel free to use these resources in presentations, websites, applications, digital products, and video projects, including commercial projects.

This collection is designed to make high-quality creative assets more accessible to everyone, supporting creativity, digital innovation, and social impact initiatives.

## Available Collections

<!-- PACKS:START -->

### Icons

| Collection                      | Quantity | Gallery                                                                 |
| ------------------------------- | -------: | ----------------------------------------------------------------------- |
| Flat Color 512                  |      300 | [View Gallery](icons/pack-01-flat-color-512/README.md)                  |
| Nusa Animals                    |      186 | [View Gallery](icons/pack-02-nusa-animals/README.md)                    |
| Nusa Buildings Construction     |      417 | [View Gallery](icons/pack-03-nusa-buildings-construction/README.md)     |
| Nusa Business Office            |      571 | [View Gallery](icons/pack-04-nusa-business-office/README.md)            |
| Nusa Celebration Culture        |      431 | [View Gallery](icons/pack-05-nusa-celebration-culture/README.md)        |
| Nusa Design Editing             |      443 | [View Gallery](icons/pack-06-nusa-design-editing/README.md)             |
| Nusa Education Science          |      298 | [View Gallery](icons/pack-07-nusa-education-science/README.md)          |
| Nusa Fashion Beauty             |      744 | [View Gallery](icons/pack-08-nusa-fashion-beauty/README.md)             |
| Nusa Files Documents            |      572 | [View Gallery](icons/pack-09-nusa-files-documents/README.md)            |
| Nusa Finance Shopping           |      627 | [View Gallery](icons/pack-10-nusa-finance-shopping/README.md)           |
| Nusa Food Drink                 |      890 | [View Gallery](icons/pack-11-nusa-food-drink/README.md)                 |
| Nusa Games Entertainment Toys   |      360 | [View Gallery](icons/pack-12-nusa-games-entertainment-toys/README.md)   |
| Nusa Health Medical             |      423 | [View Gallery](icons/pack-13-nusa-health-medical/README.md)             |
| Nusa Home Furniture             |      463 | [View Gallery](icons/pack-14-nusa-home-furniture/README.md)             |
| Nusa Industry Tools             |      182 | [View Gallery](icons/pack-15-nusa-industry-tools/README.md)             |
| Nusa Interface Navigation       |      801 | [View Gallery](icons/pack-16-nusa-interface-navigation/README.md)       |
| Nusa Law Security               |      279 | [View Gallery](icons/pack-17-nusa-law-security/README.md)               |
| Nusa Multimedia                 |      696 | [View Gallery](icons/pack-18-nusa-multimedia/README.md)                 |
| Nusa Nature Weather Environment |      658 | [View Gallery](icons/pack-19-nusa-nature-weather-environment/README.md) |
| Nusa People Emotions Gestures   |      377 | [View Gallery](icons/pack-20-nusa-people-emotions-gestures/README.md)   |
| Nusa Shapes Symbols             |      183 | [View Gallery](icons/pack-21-nusa-shapes-symbols/README.md)             |
| Nusa Sports Activities          |      349 | [View Gallery](icons/pack-22-nusa-sports-activities/README.md)          |
| Nusa Technology Devices         |      810 | [View Gallery](icons/pack-23-nusa-technology-devices/README.md)         |
| Nusa Transport Travel           |      455 | [View Gallery](icons/pack-24-nusa-transport-travel/README.md)           |
| Nusa Web Seo Social Media       |      616 | [View Gallery](icons/pack-25-nusa-web-seo-social-media/README.md)       |

### Footage

Coming soon.

See [footage/README.md](footage/README.md) for instructions on how to add new footage collections.

<!-- PACKS:END -->

## How to Use

### Download the Entire Collection

Click the green Code button at the top of this GitHub repository, then select Download ZIP.

This will download the complete collection to your device.

### Download an Individual Icon

1. Open the desired icon collection.
2. Select the SVG file you want to download.
3. Click the Download raw file button.

### Use Icons Directly on Your Website

You can link directly to SVG files using the jsDelivr CDN.

Example:

```html
<img src="https://cdn.jsdelivr.net/gh/rekan-foundation/Rekan-Icon-Pack@main/icons/pack-01-flat-color-512/idea.svg" width="64" alt="Idea">
```

If a filename contains spaces, replace each space with `%20` in the URL.

Example:

```html
<img src="https://cdn.jsdelivr.net/gh/rekan-foundation/Rekan-Icon-Pack@main/icons/pack-02-nusa-animals/FILENAME" width="64" alt="">
```

For a complete list of available files, see [manifest.json](manifest.json).

## Repository Structure

```text
icons/
  pack-01-flat-color-512/   ← One folder per collection
    pack.json               ← Title, description, and size
    README.md               ← Automatically generated gallery
    *.svg

footage/                    ← Video assets and documentation
  README.md

scripts/
  build_index.py            ← Updates galleries and manifest
```

## How to Add a New Collection

Follow these steps to add a new icon collection to the repository.

1. Create a new folder inside the icons directory using the next available sequence number.

   Example: icons/pack-26-new-collection/

2. Add your SVG or PNG files to the newly created folder.

   Naming conventions:

   * Nusa collections use the format: Nusa_Icon Name Style.svg

     Example: Nusa_Alarm Clock Flat.svg

   * Other collections use lowercase filenames with hyphens.

     Example: alarm-clock.svg

3. Create a pack.json file containing the following information:

   * title
   * description
   * size

4. Run the following command to automatically update the galleries and manifest:

   python scripts/build_index.py

5. Commit and push your changes to GitHub:

   git add .
   git commit -m "feat(icons): add pack-26"
   git push

Once completed, the new collection will be included in the repository index and available to users.

## License and Usage Rights

This collection is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

You are free to:

* Download and use the icons without payment.
* Use them for personal and educational projects.
* Incorporate them into websites, applications, presentations, and digital products.
* Modify, customize, and adapt the original icons.
* Share and redistribute the original or modified materials.
* Use them in commercial projects, products, and services.

There are no subscription fees or additional licensing fees required for the uses permitted under this license.

Attribution is required when sharing or redistributing the materials.

Please include the following credit whenever reasonably practicable:

Icon assets by Rekan Foundation
Source: github.com/rekan-foundation/Rekan-Icon-Pack
License: Creative Commons Attribution 4.0 International (CC BY 4.0)

Important Conditions:

* Do not claim the original icons as your own creation.
* Do not redistribute or sell the icons as a standalone icon pack or competing asset collection.
* Retain appropriate copyright and license notices when sharing the materials.
* Clearly indicate any modifications made to the original materials.
* Do not impose additional restrictions that prevent others from exercising their rights under the original license.

For complete legal terms, please read the [CC BY 4.0 License](LICENSE).

Official License Reference:
https://creativecommons.org/licenses/by/4.0/

## About Rekan Foundation

Rekan Foundation is committed to expanding access to creative resources, supporting digital innovation, and empowering individuals and organizations through accessible knowledge and technology.

Through Rekan Icon Pack, we aim to provide useful creative assets for nonprofit organizations, social impact institutions, designers, content creators, developers, and the wider creative community.

We believe that accessible resources can help people create better work, communicate more effectively, and generate greater impact.

FREE TO ACCESS.
FREE TO USE.
FREE TO CREATE.
FREE TO SHARE.

Made available to everyone by Rekan Foundation.
