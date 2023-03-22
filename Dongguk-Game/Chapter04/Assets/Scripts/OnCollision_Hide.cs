using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// 충돌하면 지운다
public class OnCollision_Hide : MonoBehaviour
{

    public string targetObjectName; // 목표 오브젝트 이름: Inspector에 지정
    public string hideObjectName;   // 지울 오브젝트 이름: Inspector에 지정

    // Start is called before the first frame update
    void Start()    // 처음은 아무것도 하지 않는다
    {
        
    }

    private void OnCollisionEnter2D(Collision2D collision)
    {
        // 만약 충돌한 것의 이름이 목표 오브젝트였다면
        if (collision.gameObject.name == targetObjectName)
        {
            // 지울 오브젝트를 찾아서
            GameObject hideObject = GameObject.Find(hideObjectName);
            hideObject.SetActive(false);
        }
    }
}
