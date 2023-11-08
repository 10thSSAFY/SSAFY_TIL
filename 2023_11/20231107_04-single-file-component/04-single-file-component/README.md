## Component
- 재사용 가능한 코드 블록

## Component 특징
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
- 그러면 자연스럽게 앱은 중첩된 Component의 트리로 구성됨

## Component 예시


# SFC
## Single-File Components (SFC)
- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 (*.vue 파일)

## SFC 파일 예시
- Vue SFC는 HTML, CSS 및 JavaScript 3개를 하나로 합친 것
- `<template>`, `<script>`, 및 `<style>` 블록은 하나의 파일에서 컴포넌트의 뷰, 로직 및 스타일을 캡슐화하고 배치

# SFC 문법
## SFC 문법 개요
- 각 *.vue 파일은 세 가지 유형의 최상위 언어 블록 `<template>`, `<script>`, `<style>` 으로 구성됨
- 언어 블록의 작성 순서는 상관 없으나 일반적으로 template -> script -> style 순서로 작성

## 언어 블록 _ `<template>`
- 각 *.vue 파일은 최상위 `<template>` 블록을 하나만 포함할 수 있음

## 언어 블록 _ `<script setup>`
- 각 *.vue 파일은 하나의 `<script setup>` 블록만 포함할 수 있음 (일반 `<script>` 제외)
- 컴포넌트의 `setup()` 함수로 사용되며 컴포넌트의 각 인스턴스에 대해 실행

## 언어 블록 _ `<style scope>`
- 각 *.vue 파일에는 여러 `<style>` 태그가 포함될 수 있음
- scoped가 지정되면 CSS는 현재 컴포넌트에만 적용

## 컴포넌트 사용하기
- https://play.vuejs.org/ 에서 Vue 컴포넌트 코드 작성 및 미리보기
- Vue SFC는 컴파일러를 통해 컴파일 된 후 빌드 되어야 함
- 실제 프로젝트에서는 일반적으로 SFC 컴파일러를 Vite와 같은 공식 빌드 도구를 사용해 사용

# SFC build tool (Vite)
## Vite
- 프론트 엔드 개발 도구
- 빠른 개발 환경을 위한 빌드 도구와 개발 서버를 제공
    - https://vitejs.dev/

## Vite 튜토리얼
- vite 프로젝트 생성
    - ```$ npm create vue@latest```

# NPM
## Node Package Manager (NPM)
- Node.js의 기본 패키지 관리자

## Node.js
- Chrome의 V8 JavaScript 엔진을 기반으로 하는 Server-Side 실행 환경

# Vite 프로젝트 구조
## node_modules
## package-lock.json
## package.json
## public 디렉토리
## src 디렉토리
## src/assets
## src/components
- Vue 컴포넌트들을 작성하는 곳
## src/App.vue
- Vue 앱의 최상위 Root 컴포넌트
- 다른 하위 컴포넌트들을 포함
- 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의
## scr/main.js
- Vue 인스턴스를 생성하고, 애플리케이션을 초기화하는 역할
- 필요한 라이브러리를 import 하고 전역 설정을 수행
## index.html
- Vue 앱으 기본 HTML 파일
- 앱의 진입점 (entry point)
- Root 컴포넌트인 App.vue가 해당 페이지에 마운트(mount) 됨
    - Vue 앱이 SPA인 이유
- 필요한 스타일 시트, 스크립트 등의 외부 리소스를 로드 할 수 있음 (ex. bootstrap CDN)

# 모듈과 번들러
## Module
- 프로그램을 구성하는 독립적인 코드 블록 (*.js 파일)

## Module
- 개발하는 애플리케이션의 크기가 커지고 복잡해지면서 파일 하나에 모든 기능을 담기가 어려워 짐
- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고,<br>
이때 분리된 파일 각각이 모듈(module) 즉, js 파일 하나가 하나의 모듈
- 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서<br>
특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려워 짐
- 복잡하고 깊은 모듈의 의존성 문제를 해결하기 위한 도구가 필요
    - Bundler

## node_modules의 의존성 깊이
- HEAVIEST OBJECTS IN THE UNIVERSE

## Bundler
- 여러 모듈과 파일을 하나(혹은 여러 개)의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구

## Bundler의 역할
- 의존성 관리, 코드 최적화, 리소스 관리 등
- Bundler가 하는 작업을 Bundling이라 함
- Vite는 Rollup이라는 Bundler를 사용하며 개발자가 별도로 기타 환경설정에 신경 쓰지 않도록 모두 설정해두고 있음

# Vue Componenet
## Component 활용
## 컴포넌트 사용 2단계
## 사전 준비
