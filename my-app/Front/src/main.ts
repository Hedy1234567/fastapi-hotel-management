import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { LoginComponent } from './app/login/login.component';

bootstrapApplication(LoginComponent, {
  providers: [provideRouter(routes)]
}).catch((err) => console.error(err));