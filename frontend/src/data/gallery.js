import homeCafe from "../../../assets/images/home-cafe-fausse.webp";
import interior from "../../../assets/images/gallery-cafe-interior.webp";
import ribeye from "../../../assets/images/gallery-ribeye-steak.webp";
import specialEvent from "../../../assets/images/gallery-special-event.webp";
import salmon from "../../../assets/images/supplemental-not-official/salmon-dish.jpg";
import caesar from "../../../assets/images/supplemental-not-official/caesar-salad.png";
import risotto from "../../../assets/images/supplemental-not-official/vegetable-risotto.png";
import tiramisu from "../../../assets/images/supplemental-not-official/tiramisu.jpg";
import cheesecake from "../../../assets/images/supplemental-not-official/cheesecake.png";
import espresso from "../../../assets/images/supplemental-not-official/espresso-coffee.jpg";
import chefHands from "../../../assets/images/supplemental-not-official/chef-hands.jpg";
import elegantTable from "../../../assets/images/supplemental-not-official/elegant-table.jpg";

export const officialImages = {
  home: homeCafe,
  interior,
  ribeye,
  specialEvent,
};

/** Official Quantic pack first (4 webps). Supplemental files are labeled not-official. */
export const galleryItems = [
  {
    src: interior,
    alt: "The dining room at Café Fausse",
    caption: "Interior ambiance",
    official: true,
  },
  {
    src: ribeye,
    alt: "Ribeye steak plated at Café Fausse",
    caption: "Ribeye steak from the menu",
    official: true,
  },
  {
    src: specialEvent,
    alt: "A special event at Café Fausse",
    caption: "Special events",
    official: true,
  },
  {
    src: homeCafe,
    alt: "Café Fausse",
    caption: "Café Fausse",
    official: true,
  },
  {
    src: salmon,
    alt: "Grilled salmon dish",
    caption: "Grilled salmon",
    official: false,
  },
  {
    src: caesar,
    alt: "Caesar salad",
    caption: "Caesar salad",
    official: false,
  },
  {
    src: risotto,
    alt: "Vegetable risotto",
    caption: "Vegetable risotto",
    official: false,
  },
  {
    src: tiramisu,
    alt: "Tiramisu",
    caption: "Tiramisu",
    official: false,
  },
  {
    src: cheesecake,
    alt: "Cheesecake",
    caption: "Cheesecake",
    official: false,
  },
  {
    src: espresso,
    alt: "Espresso",
    caption: "Espresso",
    official: false,
  },
  {
    src: chefHands,
    alt: "Hands preparing food in the kitchen",
    caption: "Behind the scenes",
    official: false,
  },
  {
    src: elegantTable,
    alt: "A set dining table",
    caption: "The table, ready for service",
    official: false,
  },
];
