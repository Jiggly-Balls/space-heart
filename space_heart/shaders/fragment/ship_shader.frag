#version 330

uniform sampler2D diffuseMap;
uniform sampler2D normalMap;
uniform vec2 lightPos;
uniform vec3 lightColor;
uniform float ambientStrength;

in vec2 uv;

out vec4 fragColor;

void main() {
    vec4 diffuse = texture(diffuseMap, uv);

    vec3 normal = texture(normalMap, uv).rgb * 2.0 - 1.0;
    normal = normalize(normal);

    vec3 lightDir3D = normalize(vec3(lightPos - uv, 0.5));
    float diffuseFactor = max(dot(normal, lightDir3D), 0.0);
    vec3 litColor = diffuse.rgb * (ambientStrength + diffuseFactor * (1.0 - ambientStrength)) * lightColor;

    fragColor = vec4(litColor, diffuse.a);
}