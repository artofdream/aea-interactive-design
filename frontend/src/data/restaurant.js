/** Freeze facts from docs/srs.md (official PDF SoT). Do not "improve" these. */

export const restaurant = {
  name: "Café Fausse",
  address: {
    street: "1234 Culinary Ave",
    suite: "Suite 100",
    city: "Washington, DC",
    zip: "20002",
    line: "1234 Culinary Ave, Suite 100, Washington, DC 20002",
  },
  phone: "(202) 555-4567",
  phoneHref: "tel:+12025554567",
  hours: [
    { days: "Monday–Saturday", time: "5:00 PM – 11:00 PM" },
    { days: "Sunday", time: "5:00 PM – 9:00 PM" },
  ],
  hoursLine:
    "Monday–Saturday: 5:00 PM – 11:00 PM; Sunday: 5:00 PM – 9:00 PM",
  founded: 2010,
  owners: [
    {
      name: "Chef Antonio Rossi",
      role: "Co-founder and chef",
      bio: "Chef Antonio Rossi co-founded Café Fausse in 2010. In the kitchen he blends traditional Italian flavors with modern culinary innovation, with a commitment to excellent food and locally sourced ingredients.",
    },
    {
      name: "Maria Lopez",
      role: "Co-founder and restaurateur",
      bio: "Maria Lopez co-founded Café Fausse in 2010. She leads the dining room toward an unforgettable experience that reflects both quality and creativity.",
    },
  ],
  history:
    "Founded in 2010 by Chef Antonio Rossi and restaurateur Maria Lopez, Café Fausse blends traditional Italian flavors with modern culinary innovation. Our mission is to provide an unforgettable dining experience that reflects both quality and creativity.",
  commitment:
    "We are committed to unforgettable dining, excellent food, and locally sourced ingredients.",
  awards: [
    { title: "Culinary Excellence Award", year: "2022" },
    { title: "Restaurant of the Year", year: "2023" },
    { title: "Best Fine Dining Experience", year: "Foodie Magazine, 2023" },
  ],
  reviews: [
    {
      quote: "Exceptional ambiance and unforgettable flavors.",
      source: "Gourmet Review",
    },
    {
      quote: "A must-visit restaurant for food enthusiasts.",
      source: "The Daily Bite",
    },
  ],
  tableCount: 30,
  maxGuests: 8,
};
