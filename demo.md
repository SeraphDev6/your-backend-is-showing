---
marp: true
theme: uncover
paginate: true
backgroundColor: #1a1a2e
color: #eee
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .lead {
    font-size: 1.25em;
    text-align: center;
  }
  .small {
    font-size: 0.8em;
  }
  .highlight {
    background-image: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 0.5em;
    border-radius: 8px;
  }
  .small-bullets > ul > li{
    font-size: 0.5rem;
  }
  a{
    color: white !important;
  }
---

<!-- _class: lead -->
<!-- _backgroundImage: linear-gradient(135deg, #667eea 0%, #764ba2 100%) -->

# Your Backend is Showing

## Auto-Generating Frontend SDKs So You Don't Have To

**Stop writing the same API calls twice!**

---

## Who Am I?

- **Wesley Giles**
* Python / Fast API Enthusiast
* Not good at front end work
* Believer in DRY principles
    * AKA I hate doing the same thing twice 

<!-- Speaker notes: Introduce yourself, mention your experience with APIs and the pain points you've experienced -->

---

<!-- _class: lead -->

## What We'll Cover Today

* **The Problem**: Manual API client maintenance
* **The Solution**: OpenAPI + Code Generation
* **Backend**: FastAPI & OpenAPI generation
* **Frontend**: JavaScript SDKs with HeyAPI
* **Mobile**: Flutter SDKs with openapi_generator
* **Live Demos** throughout!


---
# Why Does This Matter?
---
<!-- _class: small-bullets -->
<!-- _backgroundColor: #16213e -->


![bg left:40% opacity:0.3](https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3)

- **Consistency**: Single source of truth
- **Speed**: No more manual client updates
- **Type Safety**: Catch errors before compile time
- **Team Productivity**: Developers focus on features, not plumbing
- **Reduced Bugs**: Eliminate API contract mismatches

---

<!-- _class: lead -->
<!-- _backgroundColor: #d63031 -->

## The Old Way 😭

```javascript
// Backend changes endpoint
app.post('/api/v1/users', ...)

// Frontend developer has no idea
fetch('/api/users', {  // Wrong URL!
  method: 'POST',
  body: JSON.stringify({
    name: user.name,
    // Missing required field!
  })
})
```

**Sound familiar?**

---

<!-- _class: lead -->
<!-- _backgroundColor: #00b894 -->

## The New Way 🎉

```javascript
// Backend generates OpenAPI spec automatically
// Frontend gets type-safe client automatically

const user = await api.users.createUser({
  name: 'John Doe',
  email: 'john@example.com'  // TypeScript won't let you forget!
})
```

**Life is good.**

---

<!-- _backgroundColor: #2d3436 -->

# Backend: The Foundation

![bg right:50% w:700](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)

---

## What is OpenAPI (Swagger)?

<!-- _backgroundColor: #0984e3 -->

**OpenAPI Specification = API Contract**

```yaml
paths:
  /users:
    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - name
                - email
              properties:
                name:
                  type: string
                email:
                  type: string
```

---

## Why OpenAPI is Important

<!-- _backgroundColor: #6c5ce7 -->

* **Documentation**: (Usually) Auto-generated, (Almost) always up-to-date
* **Validation**: Request/response schema validation
* **Code Generation**: Client libraries in most languages
* **Testing**: Automated API testing
* **Tooling**: IDE support, mock servers, etc.

---

<!-- _class: lead -->
<!-- _backgroundColor: #00cec9 -->

## Why FastAPI is the Best Backend

(Fight me! 🥊)

* **Automatic OpenAPI generation** from Python type hints
* **High performance** (as fast as NodeJS/Go)
* **Modern Python** (async/await, type hints)
* **Great developer experience**
* **Built-in documentation** (Swagger UI)

---

## FastAPI Demo

<!-- _backgroundColor: #2d3436 -->

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    age: int | None = None

@app.post("/users")
async def create_user(user: User) -> User:
    # FastAPI automatically:
    # - Generates OpenAPI spec
    # - Validates request body
    # - Generates response schema
    return user
```

**That's it!** OpenAPI spec generated automatically.

<!-- Speaker notes: Show the FastAPI docs interface, demonstrate how the OpenAPI spec is generated automatically -->

---

## Other Backends? No Problem!

<!-- _backgroundColor: #e17055 -->

### Tools to Generate OpenAPI:

* **Spring Boot**: [SpringDoc OpenAPI](https://springdoc.org/)
* **ASP.NET Core**: [Swashbuckle](https://github.com/domaindrivendev/Swashbuckle.AspNetCore)
* **Express.js**: [swagger-jsdoc](https://www.npmjs.com/package/swagger-jsdoc)
* **Django**: [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)
* **Rails**: [rswag](https://github.com/rswag/rswag)
* **Elixir / Phoenix**: [Rolodex](https://hexdocs.pm/rolodex/Rolodex.html)
* **Manual**: Write YAML/JSON by hand (plz no)

---

<!-- _backgroundColor: #74b9ff -->

# Frontend: JavaScript SDKs

![bg right:30% w:200](https://raw.githubusercontent.com/hey-api/openapi-ts/main/docs/public/logo.svg)

---

## Meet HeyAPI (formerly OpenAPI TypeScript)

<!-- _backgroundColor: #0984e3 -->

* **Type-safe** client generation
* **Modern TypeScript** with excellent IDE support
* **Multiple HTTP clients** (fetch, axios, etc.)
* **Tree-shakeable** - only import what you use
* **Schema validation** with Zod
* **React Query integration** (TanStack Query)

---

## How HeyAPI Speeds Up Development

<!-- _backgroundColor: #00b894 -->
---

<!-- _backgroundColor: #00b894 -->

### Before:
* Manual API calls
* No type safety
* Documentation gets outdated
* Breaking changes break things
---

<!-- _backgroundColor: #00b894 -->

### After:
* Generated client with types
* IntelliSense and autocomplete
* Always in sync with backend
* Compile-time error checking

---

## HeyAPI Demo

<!-- _backgroundColor: #2d3436 -->

```bash
# Install HeyAPI
npm install @hey-api/openapi-ts

# Generate client from OpenAPI spec
npx @hey-api/openapi-ts \
  --input http://localhost:8000/openapi.json \
  --output ./src/client \
  --client fetch
```

---
<!-- _backgroundColor: #2d3436 -->
```typescript
// Generated client usage
import { createUser } from './client'

const {data: user, error} = await createUser({
  body: {
    name: 'John Doe',
    email: 'john@example.com'
  }
})
if(error){
  // Handle the error
}
// data is typed as the user schema! 🎉
```

<!-- Speaker notes: Show the generated client files, demonstrate autocomplete and type checking in VS Code -->

---

## Tanstack Integration Example

<!-- _backgroundColor: #6c5ce7 -->

```tsx
import { useQuery, useMutation } from '@tanstack/react-query'
import { getUsers, createUser } from './client'

function UserList() {
  const { data: users, error } = useQuery({
    queryKey: ['users'],
    queryFn: getUsers
  })

  const createMutation = useMutation({
    mutationFn: createUser
  })

  // Full type safety throughout! 🎯
}
```

---

<!-- _backgroundColor: #fd79a8 -->

## What About Mobile Apps?

![bg right:30% w:200](https://storage.googleapis.com/cms-storage-bucket/0dbfcc7a59cd1cf16282.png)

---

## Flutter SDKs with openapi_generator

<!-- _backgroundColor: #00cec9 -->

* **Dart implementation of the Official OpenAPI generator**
* 
* **Null safety** for modern Dart

---

## openapi_generator Demo

<!-- _backgroundColor: #2d3436 -->

```yaml
# Add openapi_generator to your pubspec.yaml
dependencies:
  openapi_generator_annotations: ^6.1.0
dev_dependencies:
  openapi_generator: ^6.1.0
```
```dart
@Openapi(
   additionalProperties:
   DioProperties(pubName: 'petstore_api', pubAuthor: 'Johnny dep..'),
   inputSpec:
   RemoteSpec(path: 'https://petstore3.swagger.io/api/v3/openapi.json'),
   typeMappings: {'Pet': 'ExamplePet'},
   generatorName: Generator.dio,
   runSourceGenOnOutput: true,
   outputDirectory: 'api/petstore_api',
)
class Example {} // Decorate any class to configure the generator
```
---
<!-- _backgroundColor: #2d3436 -->
### Generate and Use your SDK
```bash
flutter pub run build_runner build --delete-conflicting-outputs
```
```dart
import 'package:petstore_api/petstore_api.dart';
final apiClient = PetstoreApi().getPetsApi();
Pet[] pets = await apiClient.findPetsByStatus(status="available");
// Fully Typed  Dart Code ready to use!!
```

---

## Flutter Integration Example

<!-- _backgroundColor: #a29bfe -->

```dart
class UserService {
  final DefaultApi _api = PetstoreApi().getUserApi();
  
  Future<List<User>> getUsers() async {
    final response = await _api.getUsers();
    return response.data ?? [];
  }
  
  Future<User> createUser(String name, String email) async {
    final user = User(name: name, email: email);
    final response = await _api.createUser(user: user);
    return response.data!;
  }
}

// Use with your favorite state management solution
// Provider, Bloc, Riverpod, etc.
```

---

<!-- _backgroundColor: #00b894 -->

## The Complete Workflow


1. **Backend** generates OpenAPI spec
2. **CI/CD** triggers client generation
3. **Frontend/Mobile** gets updated SDKs
4. **Developers** use type-safe clients
5. **Profit!** 💰

<!-- Speaker notes: Explain the automation aspect and how this fits into a CI/CD pipeline -->

---

## Pro Tips & Best Practices

<!-- _backgroundColor: #eaa31eff -->

* **Version your APIs** (v1, v2, etc.)
* **Use semantic versioning** for generated clients
* **Automate generation** in CI/CD pipelines
* **Test generated clients** automatically
* **Document breaking changes** clearly
* **Consider backward compatibility**

---

<!-- _backgroundColor: #e84393 -->

## Common Gotchas

* **Date/time formats** - use ISO 8601
* **File uploads** - multipart/form-data support varies
* **Authentication** - configure properly in generators
* **Custom types** - may need manual mapping
* **Large responses** - consider pagination

---

<!-- _backgroundColor: #00cec9 -->

## Tools Ecosystem

### Other Great Options:
- **Swagger Codegen** (original, Java-based)
- **OpenAPI Generator** (community fork)
- **AutoRest** (Microsoft's generator)
- **openapi-fetch** (lightweight fetch wrapper)
- **Orval** (React Query + MSW integration)

---

<!-- _class: lead -->
<!-- _backgroundImage: linear-gradient(135deg, #667eea 0%, #764ba2 100%) -->

## Demo Time! 🚀

Let's see it all working together:

1. FastAPI backend with auto-generated OpenAPI
2. Generated TypeScript client with HeyAPI
3. Generated Dart client for Flutter
4. Live updates when API changes

---

<!-- _backgroundColor: #2d3436 -->

## Key Takeaways

* **Stop writing API clients manually**
* **OpenAPI is your single source of truth**
* **FastAPI makes backend development joy**
* **HeyAPI generates excellent TypeScript clients**
* **openapi_generator supports mobile apps**
* **Automation saves time and reduces bugs**

---

<!-- _backgroundColor: #00b894 -->

## Resources

* **FastAPI**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
* **HeyAPI**: [heyapi.vercel.app](https://heyapi.vercel.app)
* **OpenAPI Generator**: [openapi-generator.tech](https://openapi-generator.tech)
* **OpenAPI Spec**: [spec.openapis.org](https://spec.openapis.org)
<!-- * **Example Code**: [github.com/yourrepo/sdk-demo](https://github.com/yourrepo/sdk-demo) -->

---

<!-- _class: lead -->
<!-- _backgroundImage: linear-gradient(135deg, #ff7675 0%, #74b9ff 100%) -->

# Questions?

## Let's eliminate manual API calls together! 

**Thank you!**

<!-- Add your contact information here -->
📧 Wesley@seraphdev.com
🐙 [github.com/SeraphDev6](https://github.com/SeraphDev6)

