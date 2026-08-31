import { restaurant } from "../data/restaurant.js";

export default function Hours() {
  return (
    <ul className="hours-list">
      {restaurant.hours.map((row) => (
        <li key={row.days}>
          <span>{row.days}</span>
          <span>{row.time}</span>
        </li>
      ))}
    </ul>
  );
}
