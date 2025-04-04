import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

// Exemple de modèle d'hôtel
interface Hotel {
  name: string;
  address: string;
  stars: number;
}

@Component({
  selector: 'app-hotel-listing',
  templateUrl: './hotel-listing.component.html',
  imports: [CommonModule],
  styleUrls: ['./hotel-listing.component.css']
})
export class HotelListingComponent {
  hotels: Hotel[] = [
    { name: 'Hotel Paris', address: '12 Rue de Rivoli, Paris', stars: 5 },
    { name: 'Hotel Cairo', address: '123 Nile St, Cairo', stars: 4 },
    { name: 'Hotel Berlin', address: '45 Alexanderplatz, Berlin', stars: 3 }
  ];
}
